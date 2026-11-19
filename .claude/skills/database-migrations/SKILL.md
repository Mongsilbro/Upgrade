---
name: database-migrations
description: "Use when writing or reviewing a schema or data migration: column/index/constraint changes, backfills, rollback, zero-downtime deploys."
---

# Database migrations

Adapted from [affaan-m/ECC](https://github.com/affaan-m/ECC) `skills/database-migrations/` (`SKILL.md` and `examples/*.sql`), MIT License, Copyright (c) 2026 Affaan Mustafa. Rewritten and condensed; tool-specific command lists dropped (use the tool's own docs).

## Principles

1. Every change is a migration file under version control; no manual changes to production.
2. A migration that has run anywhere shared is never edited; fix it with a new one.
3. Production goes forward only: undo with a new forward migration. Still write the down step (or mark it irreversible) for development.
4. Schema changes (DDL) and data changes (backfills) are separate migrations.
5. Think at production size: what is fine on 100 rows can lock a table for minutes on 10 million.

## Before applying, check

- [ ] Which lock each statement takes and for how long. In PostgreSQL most `ALTER TABLE` forms take `ACCESS EXCLUSIVE`, even when no rewrite happens; set `lock_timeout` and keep the transaction short.
- [ ] New columns on populated tables are nullable or have a constant default. A `NOT NULL` column without default fails on existing rows. A volatile default (e.g. `clock_timestamp()`) rewrites the table.
- [ ] Indexes on existing large tables built without blocking writes (`CREATE INDEX CONCURRENTLY`, outside a transaction — most tools need a flag or a raw-SQL migration for this).
- [ ] New constraints added in a non-blocking way where the database supports it (PostgreSQL: `NOT VALID`, then `VALIDATE CONSTRAINT` separately).
- [ ] Backfills run in committed batches, are safe to rerun, and do not load values into application memory to write back later.
- [ ] Code stops using a column before the migration that drops it ships.
- [ ] Tested against a copy of production-sized data; rollback plan written down.

## Expand–contract (rename, change type, split a column)

Never rename in place under live traffic. Instead:

1. **Expand:** add the new column (nullable).
2. Deploy code that reads the old column and writes **both**, on every write path (jobs, imports, admin tools included). Wait until no old-only writer or in-flight transaction remains.
3. **Backfill** in key ranges, each committed separately, copying the current value in the same `UPDATE`:
   `UPDATE t SET new = old WHERE id > :a AND id <= :b AND new IS DISTINCT FROM old;`
   `IS DISTINCT FROM` also repairs stale non-null values and handles NULLs; a `WHERE new IS NULL` backfill cannot fix values that changed after copying.
4. **Verify:** `SELECT count(*) FROM t WHERE new IS DISTINCT FROM old;` must be 0 before switching reads.
5. Deploy code that reads the new column, still writing both, for the whole rollback window.
6. **Contract:** move constraints, indexes, and dependants (views, reports, other services) to the new column; deploy code using only the new column; then drop the old column in a separate migration.

Once writes go only to the new column, the old one is stale: rolling back to old readers needs a reconciliation step first.

## Review output

For each migration, state: statements and their lock level, estimated rows touched, whether it can run during traffic, how it is undone, and anything that must be deployed before or after it.

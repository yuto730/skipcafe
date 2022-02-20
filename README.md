# データベース設計

## contacts テーブル

| Column            | Type   | Options                        |
| ----------------- | ------ | ------------------------------ |
| name              | string | null: false                    |
| url               | text   |                                |
| mail              | string | null: false                    |
| mail_confirmation | string | null: false                    |
| message           | text   | null: false                    |


## users テーブル

| Column                | Type     | Options     |
| --------------------- | -------- | ----------- |
| user_name             | string   | null: false |
| email                 | string   | null: false |
| password              | string   | null: false |
| password_confirmation | string   | null: false |
| first_name            | string   | null: false |
| last_name             | string   | null: false |
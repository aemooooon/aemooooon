---
layout: post
subtitle: PostgREST
categories: [PostgreSQL]
header:
    image: header.jpg
    align:
    text: light
---

# PostgreSQL

## 

# PostgREST

## Run PostgresSQL in local Mac with docker

```bash
sudo docker run --name tutorial -p 5433:5432 \
                -e POSTGRES_PASSWORD=mysecretpassword \
                -d postgres

sudo docker exec -it tutorial psql -U postgres

create schema api;

create table api.todos (
  id serial primary key,
  done boolean not null default false,
  task text not null,
  due timestamptz
);

insert into api.todos (task) values
  ('finish tutorial 0'), ('pat self on back');

# 创建 web_anon 角色，并设置其为非登录角色（nologin）
create role web_anon nologin; 

# 授予web_anon对api模式的使用权限
grant usage on schema api to web_anon; 
# 授予web_anon对api.todos表的查询（CRUD only with R）权限
grant select on api.todos to web_anon; 

# 创建 authenticator 登录角色，不继承其他角色
create role authenticator noinherit login password 'mysecretpassword'; 
# 授予 web_anon 角色 to authenticator 角色，使其继承web_anon的权限（api模式和api.todos表的查询权限）
grant web_anon to authenticator; 

\q
```

## Install PostgREST on Mac

```bash
brew install postgrest

create `conf` file: tutorial.conf

db-uri = "postgres://authenticator:mysecretpassword@localhost:5433/postgres"
db-schemas = "api"
db-anon-role = "web_anon"

postgrest tutorial.conf

curl http://localhost:3000/todos
```

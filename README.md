# ansible-role-php-fpm

CentOS 7 に php-fpm を構築する ansible role です。

## 設定項目

以下の設定項目は上書き可能。

項目名           |デフォルト値|説明
-----------------|------------|-------------------------------------
php_fpm_www      |apache      |連携させる Web サーバ（apache|nginx）

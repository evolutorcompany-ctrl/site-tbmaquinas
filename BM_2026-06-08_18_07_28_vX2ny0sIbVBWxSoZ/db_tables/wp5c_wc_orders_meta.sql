/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_wc_orders_meta`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_wc_orders_meta`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_wc_orders_meta` ( `id` bigint unsigned NOT NULL AUTO_INCREMENT, `order_id` bigint unsigned DEFAULT NULL, `meta_key` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci DEFAULT NULL, `meta_value` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci, PRIMARY KEY (`id`), KEY `order_id_meta_key_meta_value` (`order_id`,`meta_key`(100),`meta_value`(82)), KEY `meta_key_value` (`meta_key`(50),`meta_value`(20))) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

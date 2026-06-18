/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_woocommerce_order_itemmeta`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_woocommerce_order_itemmeta`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_woocommerce_order_itemmeta` ( `meta_id` bigint unsigned NOT NULL AUTO_INCREMENT, `order_item_id` bigint unsigned NOT NULL, `meta_key` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci DEFAULT NULL, `meta_value` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci, PRIMARY KEY (`meta_id`), KEY `order_item_id` (`order_item_id`), KEY `meta_key` (`meta_key`(32))) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

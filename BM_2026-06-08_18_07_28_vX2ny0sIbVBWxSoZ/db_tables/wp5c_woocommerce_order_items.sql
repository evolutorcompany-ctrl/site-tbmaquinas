/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_woocommerce_order_items`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_woocommerce_order_items`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_woocommerce_order_items` ( `order_item_id` bigint unsigned NOT NULL AUTO_INCREMENT, `order_item_name` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL, `order_item_type` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '', `order_id` bigint unsigned NOT NULL, PRIMARY KEY (`order_item_id`), KEY `order_id` (`order_id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_wc_order_stats`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_wc_order_stats`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_wc_order_stats` ( `order_id` bigint unsigned NOT NULL, `parent_id` bigint unsigned NOT NULL DEFAULT '0', `date_created` datetime NOT NULL DEFAULT '0000-00-00 00:00:00', `date_created_gmt` datetime NOT NULL DEFAULT '0000-00-00 00:00:00', `date_paid` datetime DEFAULT '0000-00-00 00:00:00', `date_completed` datetime DEFAULT '0000-00-00 00:00:00', `num_items_sold` int NOT NULL DEFAULT '0', `total_sales` double NOT NULL DEFAULT '0', `tax_total` double NOT NULL DEFAULT '0', `shipping_total` double NOT NULL DEFAULT '0', `net_total` double NOT NULL DEFAULT '0', `returning_customer` tinyint(1) DEFAULT NULL, `status` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL, `customer_id` bigint unsigned NOT NULL, PRIMARY KEY (`order_id`), KEY `date_created` (`date_created`), KEY `customer_id` (`customer_id`), KEY `status` (`status`), KEY `idx_date_paid_status_parent` (`date_paid`,`status`,`parent_id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

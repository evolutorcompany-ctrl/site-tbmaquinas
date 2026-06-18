/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_wc_reserved_stock`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_wc_reserved_stock`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_wc_reserved_stock` ( `order_id` bigint NOT NULL, `product_id` bigint NOT NULL, `stock_quantity` double NOT NULL DEFAULT '0', `timestamp` datetime NOT NULL DEFAULT '0000-00-00 00:00:00', `expires` datetime NOT NULL DEFAULT '0000-00-00 00:00:00', PRIMARY KEY (`order_id`,`product_id`), KEY `product_id_expires` (`product_id`,`expires`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

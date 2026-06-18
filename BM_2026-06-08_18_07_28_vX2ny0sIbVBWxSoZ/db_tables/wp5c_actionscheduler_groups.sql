/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_actionscheduler_groups`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_actionscheduler_groups`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_actionscheduler_groups` ( `group_id` bigint unsigned NOT NULL AUTO_INCREMENT, `slug` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL, PRIMARY KEY (`group_id`), KEY `slug` (`slug`(191))) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
INSERT INTO `1780942049_wp5c_actionscheduler_groups` (`group_id`, `slug`) VALUES (1,'action-scheduler-migration'),(2,''),(3,'wc_update_product_lookup_tables'),(4,'wpforms'),(5,'woocommerce-db-updates'),(6,'wc_update_product_default_cat'),(7,'woocommerce-remote-inbox-engine'),(8,'wp_mail_smtp'),(9,'count'),(10,'ActionScheduler'),(11,'woocommerce');

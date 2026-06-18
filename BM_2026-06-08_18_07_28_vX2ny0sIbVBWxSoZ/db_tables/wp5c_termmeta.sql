/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_termmeta`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_termmeta`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_termmeta` ( `meta_id` bigint unsigned NOT NULL AUTO_INCREMENT, `term_id` bigint unsigned NOT NULL DEFAULT '0', `meta_key` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci DEFAULT NULL, `meta_value` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci, PRIMARY KEY (`meta_id`), KEY `term_id` (`term_id`), KEY `meta_key` (`meta_key`(191))) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
INSERT INTO `1780942049_wp5c_termmeta` (`meta_id`, `term_id`, `meta_key`, `meta_value`) VALUES (1,25,'order',0),(2,25,'_astra_sites_imported_term',1),(3,26,'order',0),(4,26,'_astra_sites_imported_term',1),(5,27,'_astra_sites_imported_term',1),(10,31,'_astra_sites_imported_term',1),(12,25,'product_count_product_cat',4),(13,26,'product_count_product_cat',1),(14,17,'display_type',''),(15,17,'thumbnail_id',0),(16,17,'product_count_product_cat',1),(17,26,'display_type',''),(18,26,'thumbnail_id',0),(19,25,'display_type',''),(20,25,'thumbnail_id',0);

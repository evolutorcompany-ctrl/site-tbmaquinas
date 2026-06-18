/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_term_relationships`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_term_relationships`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_term_relationships` ( `object_id` bigint unsigned NOT NULL DEFAULT '0', `term_taxonomy_id` bigint unsigned NOT NULL DEFAULT '0', `term_order` int NOT NULL DEFAULT '0', PRIMARY KEY (`object_id`,`term_taxonomy_id`), KEY `term_taxonomy_id` (`term_taxonomy_id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
INSERT INTO `1780942049_wp5c_term_relationships` (`object_id`, `term_taxonomy_id`, `term_order`) VALUES (11,2,0),(21,3,0),(26,20,0),(26,24,0),(27,21,0),(27,24,0),(5015,1,0),(5458,33,0),(5466,20,0),(5466,34,0),(5467,21,0),(5467,34,0),(5490,36,0),(5491,36,0),(5492,36,0),(5503,4,0),(5503,10,0),(5503,25,0),(5852,4,0),(5852,10,0),(5852,26,0),(5856,4,0),(5856,10,0),(5856,17,0),(5888,31,0),(5991,4,0),(5991,10,0),(5991,25,0),(6409,4,0),(6409,10,0),(6409,25,0),(6493,31,0),(6497,4,0),(6497,10,0),(6497,25,0),(6575,31,0);

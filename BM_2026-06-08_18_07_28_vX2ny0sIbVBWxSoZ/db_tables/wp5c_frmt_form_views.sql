/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_frmt_form_views`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_frmt_form_views`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_frmt_form_views` ( `view_id` bigint unsigned NOT NULL AUTO_INCREMENT, `form_id` bigint unsigned NOT NULL, `page_id` bigint unsigned NOT NULL, `ip` varchar(191) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci DEFAULT NULL, `count` mediumint unsigned NOT NULL DEFAULT '1', `date_created` datetime NOT NULL DEFAULT '0000-00-00 00:00:00', `date_updated` datetime NOT NULL DEFAULT '0000-00-00 00:00:00', PRIMARY KEY (`view_id`), KEY `view_form_id` (`form_id`), KEY `view_ip` (`ip`), KEY `view_form_object` (`form_id`,`view_id`), KEY `view_form_object_ip` (`form_id`,`view_id`,`ip`)) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
INSERT INTO `1780942049_wp5c_frmt_form_views` (`view_id`, `form_id`, `page_id`, `ip`, `count`, `date_created`, `date_updated`) VALUES (1,6214,5914,NULL,1,'2023-10-22 21:40:52','0000-00-00 00:00:00');

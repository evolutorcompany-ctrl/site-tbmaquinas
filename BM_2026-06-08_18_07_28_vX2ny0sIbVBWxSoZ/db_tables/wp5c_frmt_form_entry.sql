/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_frmt_form_entry`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_frmt_form_entry`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_frmt_form_entry` ( `entry_id` bigint unsigned NOT NULL AUTO_INCREMENT, `entry_type` varchar(191) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL, `draft_id` varchar(12) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci DEFAULT NULL, `form_id` bigint unsigned NOT NULL, `is_spam` tinyint(1) NOT NULL DEFAULT '0', `date_created` datetime NOT NULL DEFAULT '0000-00-00 00:00:00', PRIMARY KEY (`entry_id`), KEY `entry_is_spam` (`is_spam`), KEY `entry_type` (`entry_type`), KEY `entry_form_id` (`form_id`)) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
INSERT INTO `1780942049_wp5c_frmt_form_entry` (`entry_id`, `entry_type`, `draft_id`, `form_id`, `is_spam`, `date_created`) VALUES (1,'custom-forms',NULL,6214,0,'2023-10-22 21:41:34');

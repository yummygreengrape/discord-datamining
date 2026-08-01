# Discord string context report — 2026-08-01

- Generated: `2026-08-01T09:12:57.625Z`
- Period: `2026-07-30T14:58:18Z` to `2026-08-01T06:47:40.798496+00:00`
- Build: `df6526438f716e196f36c4aa57781c3462616550`
- Clusters: 8
- Annotated strings: 80
- Deferred: 1056
- `latest_changes.json` string_context keys: 5 Korean / 0 English

## Outcome

The source window contained 366 string rows. This run annotated 80 rows across 8 clusters and deferred 286 new-window rows. The ignored public history snapshot imported 10 source rows and was synchronized to build df6526438f716e196f36c4aa57781c3462616550.

## Annotated clusters

### Inactive Group DM bulk cleanup

- Keys: `+HM0x2`, `2Cgdhl`, `FCwJId`, `FLgBG/`, `FrCK4r`, `NLTGck`, `RQbtb8`, `SHTZTm`, `VHmOpK`, `YBjUwi`, `mKxGpP`
- Intent: `feature_or_setting_explanation`
- Confidence: `high`
- Rows: 38
- Summary: 약 6개월 동안 활동이 없는 그룹 DM을 정렬·선택해 최대 1,000개까지 알림 없이 한꺼번에 나가는 정리 기능의 문구입니다.
- English: Copy for sorting and selecting Group DMs inactive for about six months, then leaving up to 1,000 of them without notifying participants.
- Evidence: 같은 변경 묶음에 `Clean Up Inactive Group DMs`, 최대 1,000개·약 6개월 기준, 무알림 나가기, rate-limit과 실패 문구가 추가됐고 최신 리포트는 bulk-leave API를 함께 확인했습니다.

### Audio input and output device suggestions

- Keys: `1l/LhA`, `Jat8cd`, `RJttRt`, `SupmjL`, `VLKyL8`, `xYe9fZ`
- Intent: `voice_video_or_device_issue`
- Confidence: `medium`
- Rows: 12
- Summary: Discord가 새 마이크나 스피커를 감지했을 때 입력·출력 장치를 바꿀지 묻는 음성 장치 제안 문구입니다.
- English: A Discord voice prompt asking whether to switch input, output, or both after a new microphone or speaker is detected.
- Evidence: 현재 문자열과 최신 리포트의 `2026-07-unobtrusive-device-suggestions` 소비자 근거가 switch, dismiss, ignore 동작을 같은 DeviceDetectedPanel에 연결합니다.

### Conjuring project, preview, and publish errors

- Keys: `1RCbQT`, `6L9Vwt`, `GnEJ3o`, `IHCafX`, `IN/HRP`, `MeLWCr`, `fNP6Cd`, `wjWm+/`
- Intent: `error_or_blocked_action`
- Confidence: `high`
- Rows: 8
- Summary: Discord의 Conjuring 앱 제작 흐름에서 계획·연결·미리보기·빌드·게시가 완료되지 않았음을 알리는 오류 문구입니다.
- English: Error copy for unfinished planning, connection, preview, build, or publish steps in Discord's Conjuring app-builder flow.
- Evidence: 현재 `2026-07-vibegrations-guild` 소비자와 최신 리포트는 Manage Channels·Manage Guild 조건의 앱 빌더가 Conjuring 용어로 바뀌었고 동일 창에 구체적 오류 상태가 추가됐음을 확인합니다.

### Conjuring preview and publish permission review

- Keys: `+UouPe`, `5gU57O`, `CRfE/E`, `DYwf2n`, `E0QD++`, `Rtlv25`, `WWj3pN`, `nDQB/b`
- Intent: `server_or_permission_notice`
- Confidence: `high`
- Rows: 8
- Summary: Conjuring으로 만든 서버 앱을 미리보기·게시하기 전에 새 권한을 검토하고 승인해야 한다는 안내입니다.
- English: A notice that newly requested permissions must be reviewed before a Conjuring project can be previewed or published.
- Evidence: 현재 문자열은 Review permissions, preview 차단, publish 차단과 게시 성공을 한 묶음으로 추가했고, `2026-07-vibegrations-guild` 근거는 이를 서버 권한이 필요한 앱 제작 흐름에 연결합니다.

### Age verification selfie and on-device biometric notice

- Keys: `fm7qBC`, `rgXXcW`
- Intent: `account_or_safety_notice`
- Confidence: `high`
- Rows: 2
- Summary: Discord 연령 확인에서 셀피를 선택할 수 있고, 화면상 안내는 생체 정보가 기기 안에서 처리되어 기기를 떠나지 않는다고 설명합니다.
- English: An age-verification selfie option whose on-screen notice says biometric data is processed locally and does not leave the device.
- Evidence: 같은 변경 창에서 셀피 문구와 개인정보 설명이 수정됐고, 최신 리포트는 VERIFY_AGE_V2·AGE_SIGNAL·AGE_SIGNAL_CHALLENGE 경로를 함께 확인했습니다.

### Clips Gallery profile widget

- Keys: `7AVpta`, `FEcbkU`, `RFRuwZ`, `rI0i0a`, `xcLXWy`, `zrtAwA`
- Intent: `feature_or_setting_explanation`
- Confidence: `high`
- Rows: 6
- Summary: Discord 프로필의 Clips Gallery 위젯에 게임 클립을 추가하고 순서를 정해 보여 주는 기능 문구입니다.
- English: Copy for adding gameplay clips to a Clips Gallery widget and arranging what the widget shows on a Discord profile.
- Evidence: 현재 Canary localization이 Add Clips Gallery Widget, Add Clip, Uploading clip, Show clip과 게임 클립 제한을 기존 Profile Widgets 묶음 안에 직접 배치합니다.

### Profile Widget image upload failure

- Keys: `F4Neqh`
- Intent: `error_or_blocked_action`
- Confidence: `high`
- Rows: 2
- Summary: Discord Profile Widgets 편집기에서 이미지 블록 업로드가 완료되지 않았다는 오류입니다.
- English: An error indicating that an image block did not upload in the Discord Profile Widgets editor.
- Evidence: 현재 Canary localization이 Image upload failed를 Add Image, Remove Image, Profile Widgets 편집 라벨과 같은 묶음에 둡니다.

### Server Hub panels and save state

- Keys: `HmFYc5`, `IuT87w`, `L8Xfoo`, `N8nJ+T`
- Intent: `feature_or_setting_explanation`
- Confidence: `high`
- Rows: 4
- Summary: Server Hub 페이지에 패널을 추가하고 드래그해 배치하는 편집 화면과 저장 실패 문구입니다.
- English: Copy for adding panels to a Server Hub page, arranging them by drag and drop, and reporting a save failure.
- Evidence: 현재 문자열이 Server Hub와 Add Panel을 직접 연결하고, `2026-06_guild_spaces` 실험 및 space/widget API가 서버 관리 허브 표면을 확인합니다.

## Deferred

- Carry-forward entries retained: 770
- Prior deferred entries superseded by current analyzed rows: 11
- New-window entries deferred: 286
- `new_window_not_selected_within_run_cap`: 266
- `deleted_without_current_consumer`: 186
- `bulk_deleted_campaign_copy_not_selected`: 169
- `current_translation_or_copy_not_selected`: 129
- `low_context_label`: 128
- `vibegrations_cluster_cap_not_selected`: 89
- `group_dm_cluster_cap_not_selected`: 33
- `deleted_campaign_or_copy_not_selected`: 19
- `malformed_extraction_or_deleted_copy`: 13
- `deleted_replaced_copy`: 11
- `translation_polish_low_search_intent`: 5
- `copy_polish_or_context_not_selected`: 4
- `internal_or_low_public_context`: 2
- `placeholder_low_context`: 1
- `deleted_low_context_label`: 1

Representative deferred items:

- Remaining Group DM cleanup empty states, progress counters, and secondary controls stay deferred for a later bounded pass.
- Remaining Conjuring status, logs, project management, and fantasy-styled labels stay deferred after the error and permission surfaces selected here.
- Deleted Riot connection migration copy remains historical deletion evidence and does not establish the current service state.
- Guild Rooms notes and seat/object labels remain deferred until their standalone visitor search intent is stronger.
- Generic feedback choices, short labels, formatting fragments, and malformed `bHook` deletion rows were not forced into public analysis.

## Search signals

- Search Console was not used.
- Public Google results were not required; current localization, APIs, experiments, and the latest evidence-backed report were sufficient.
- Public search snippets remain secondary signals for future sparse or ambiguous windows.

## Validation and publish

- Status: `passed`
- `passed` — python3 -m json.tool data/web/meta.json
- `passed` — python3 -m json.tool data/web/strings.ko.json
- `passed` — python3 -m json.tool data/web/strings.en.json
- `passed` — python3 -m json.tool data/latest_changes.json
- `passed` — python3 -m json.tool data/reports/string-context/latest.json
- `passed` — python3 -m json.tool data/reports/string-context/2026-08-01.json
- `passed` — python3 -m json.tool data/history.json
- `passed` — 10 source rows imported without core payload changes
- `passed` — 80 selected analysis-row changes
- `passed` — history/source/web full-row and annotation parity
- `passed` — 80-row paired required-field and English-language checks
- `passed` — analysis-only tracked web comparison
- `passed` — latest string_context limited to current payload keys
- `passed` — scoped private-path, token, SEO, and overclaim scan
- `passed` — report JSON/Markdown pointer parity
- `passed` — compact tracked web JSON
- `passed` — python3 scripts/security_scan.py --root . .
- `passed` — python3 -m unittest discover -s tests -p 'test_*.py'
- `passed` — ./scripts/check_security.sh (private runner)
- `passed` — git diff --check
- `passed` — data commit pushed to origin/main

- Data commit: `837f9bc7` — Add August 1 string context interpretations (pushed: true)

## Security/privacy impact

No trust boundary, collection field, storage recipient, retention rule, deletion path, or access control changed. This run adds only public Discord product-string interpretation metadata, a narrow latest-payload context map, and report artifacts. It adds no user content, identifiers, credentials, private runner state, or new external recipient.

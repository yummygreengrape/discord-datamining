# Discord Datamining Weekly Report - 2026-07-22

- 처리 기간: `2026-07-18T04:06:34Z` - `2026-07-22T04:03:13Z`
- 실행 시각: `2026-07-22 13:03:13 KST`
- build_hash: `04691e324fae0e29375c984ba38e3614523240ab`
- 근거 번들: `canary/web.cb79fa6ccb8b06a4.js`
- 입력 기준: `data/history.json`을 우선 확인하고 tracked `data/web/*`와 대조했습니다. local history에서 빠진 실험 19개와 문자열 272개를 복구했으며, `latest_changes.json`은 현재 빌드의 마지막 수정 1건을 확인하는 보조 신호로만 사용했습니다.

## 핵심 요약

- 이번 처리 창에는 실험 19행, API 0행, 문자열 272행이 있습니다. 실제 화면 소비가 확인된 2개를 새로 해석하고 기존 Nitro 혜택 표시 해석 1개를 현재 수정 행에 다시 동기화했습니다.
- 1:1 DM에서 그룹 DM을 만들 때 제목과 현재 상대 표시를 명확히 하는 흐름, 지원 기기에서 음성 출력 메뉴에 공간 음향 스위치를 노출하는 흐름이 현재 Canary 소비 코드로 확인됐습니다.
- 사용자 화면 가능성은 있지만 실험 연결이 부족한 4개는 새 unresolved로 남겼고, 11개 삭제 행은 보존할 기존 해석이 없어 deletion-only로 분류했습니다. 통화 종료 시 GPU 관련 행은 사용자 화면이 확인되지 않아 내부/저가치로 분류했습니다.
- 실험 외에는 메시지 유형별 알림, 게임 서버 관리, Nitro 체험·할인 가격, 게임 계정 연결, 활동 접근성, 게임 프로필과 Clips 품질 문구가 주요 변화입니다.

## 실험 전수 분석 결과

### interpreted

| id | timestamp | status | reason | evidence_notes |
| --- | --- | --- | --- | --- |
| 2026-07-create-gdm-title | 2026-07-21T20:40:40Z | added | the one-to-one DM invite modal reads enabled and changes the group-creation title and current-recipient tag | The modal switches Add to DM to Create New Group DM and locks the current recipient in the picker. |
| 2026-05-spatial-audio-for-voice | 2026-07-22T01:21:07.694229+00:00 | modified | the audio-device menu reads the flag and hardware support before showing a working Spatial Audio switch | The matching label became user-facing in the same build, and the switch updates the current voice setting. |

### strengthened_existing

| id | timestamp | status | reason | evidence_notes |
| --- | --- | --- | --- | --- |
| 2026-06-ml-offer-creation-ui-upgrade | 2026-07-20T18:29:19.509469+00:00 | modified | the current Nitro tab consumer reconfirms badge style and explanation surface; the settings remain unchanged | NitroTabButton still reads badgeStyle and surface in the current Canary bundle. |

### unresolved_needs_evidence

| id | timestamp | status | reason | evidence_notes |
| --- | --- | --- | --- | --- |
| 2026-07-wishlist-direct-to-gifting | 2026-07-21T16:05:07Z | added | wishlist and gifting flows exist, but no exact experiment match or variant consumer links them to this row | Current wishlist routes and gift UI are product evidence only; the experiment linkage remains unconfirmed. |
| 2026-06-guild-profile-server-tag | 2026-07-21T17:09:42Z | added | server-tag state and profile copy exist, but no exact experiment match or config consumer connects this row to the visible profile | The existing mobile server-tag registration is separate and still has no assigned result. |
| 2026-06-game-server-hosting-in-shop | 2026-07-21T18:01:14Z | added | Shop and game-server management copy confirm the product surface, but no exact experiment or treatment consumer was found | Game-server subscription, cancellation, and Shop strings are strong surface evidence without experiment linkage. |
| 2026-07-powerups-coachmark-scroll-close | 2026-07-21T23:35:16Z | added | Powerups coachmark code exists, but no exact experiment match or scroll-close consumer links that behavior to this row | The related older mobile coachmark flag still only gates data fetching in GuildPowerupsManager. |

### internal_or_low_value

| id | timestamp | status | reason | evidence_notes |
| --- | --- | --- | --- | --- |
| 2026-07-reduce-leave-call-gpu | 2026-07-21T20:43:42Z | added | no exact experiment match, user-facing string, or visible surface was found for this low-level call-exit change | Current leave-call and media paths did not expose a behavior-linked config consumer. |

### deletion_only_no_context

| id | timestamp | status | reason | evidence_notes |
| --- | --- | --- | --- | --- |
| 2026-04-game-account-linking-post-game-close | 2026-07-20T18:51:31Z | deleted | deleted without a prior evidence-backed interpretation or a current experiment consumer | Nearby connection-migration copy does not establish that this experiment controlled the post-game prompt. |
| 2025-10-layer-system-v2 | 2026-07-20T21:27:50Z | deleted | deleted without a prior evidence-backed interpretation or a current consumer to preserve | No current exact id match or behavior-linked layer-system read was found. |
| 2026-05-logitech-ss-reheat-ff | 2026-07-20T22:44:29Z | deleted | deleted without a prior evidence-backed interpretation or a current consumer to preserve | The same extraction removes Logitech perk copy, but that does not prove rollout or rollback for this id. |
| 2026-04-croissant-reheat | 2026-07-20T22:44:29Z | deleted | deleted with only an enabled flag and no confirmed user-facing surface | No current exact id match, string linkage, or config consumer was found. |
| 2026-05-steelseries-higher-discount-ff | 2026-07-20T22:50:12.546128+00:00 | deleted | deleted without a prior evidence-backed interpretation or a current consumer to preserve | Partner-benefit copy was also removed, but the experiment-to-surface linkage is not confirmed. |
| 2026-05-kontrolfreek-deprecated-ff | 2026-07-20T22:50:12.546128+00:00 | deleted | deleted without a prior evidence-backed interpretation or a current consumer to preserve | No current exact id match or product-surface consumer was found. |
| 2026-03-steelseries-3p-recurring | 2026-07-20T22:50:12.546128+00:00 | deleted | deleted without a prior evidence-backed interpretation or a current consumer to preserve | The current client no longer exposes an exact id or confirmed recurring-benefit consumer. |
| 2026-03-l-3pp | 2026-07-20T22:50:12.546128+00:00 | deleted | deleted with no prior interpretation and no evidence beyond the raw enabled flag | No exact id, route, string, or user-facing config consumer was found. |
| 2026-02-android-app-upsell-banner | 2026-07-21T01:48:01Z | deleted | deleted without a prior evidence-backed interpretation or a current Android upsell consumer | No public analysis was added and the deletion is not treated as a rollout decision. |
| 2026-04-quest-heartbeat-executable-fingerprint | 2026-07-21T17:07:26.575751+00:00 | deleted | deleted without a prior evidence-backed interpretation or a current heartbeat consumer | No exact id or executable-fingerprint read remains in the current bundle. |
| 2026-04-user-settings-redesign-4c | 2026-07-21T23:15:04Z | deleted | deleted after several earlier add/delete events, with no prior evidence-backed interpretation to preserve | Settings labels were removed nearby, but no current experiment consumer establishes the affected layout. |

## 중요한 실험 상세 해석

### 1:1 DM에서 새 그룹 DM 만들기

- id: `2026-07-create-gdm-title`
- 요약: 기존 1:1 DM에 사람을 더해 그룹 DM을 만들 때, 초대 창 제목과 현재 대화 상대 표시를 더 명확하게 보여 주는 실험입니다.
- 근거: 기존 1:1 DM의 초대 창이 설정값을 읽어 제목을 ‘새 그룹 DM 만들기’로 바꾸고 현재 상대를 제거할 수 없는 선택 항목으로 표시합니다.
- source_context: DM invite modal, Create New Group DM, titleExperimentEnabled

### 음성 통화 공간 음향 스위치

- id: `2026-05-spatial-audio-for-voice`
- 요약: 음성 통화의 출력 장치 메뉴에 공간 음향 스위치를 표시해, 지원되는 기기에서 입체적인 음성 배치를 켜고 끌 수 있게 하는 실험입니다.
- 근거: 출력 장치 메뉴가 설정값과 기기 지원 여부를 함께 확인한 뒤 공간 음향 스위치를 표시하고 현재 통화 설정을 변경합니다.
- source_context: Audio Device Menu, Spatial Audio, hardware support check

### Nitro 맞춤 혜택 표시 재확인

- id: `2026-06-ml-offer-creation-ui-upgrade`
- 요약: Nitro 탭의 맞춤 혜택 배지 모양과 안내 방식을 바꾸는 기존 해석을 현재 수정 행에 다시 동기화했습니다.
- 근거: 이번 수정 행의 기본값과 비교안은 이전과 같고, 현재 Nitro 탭 버튼이 badgeStyle과 surface를 계속 읽습니다.
- source_context: NitroTabButton, badgeStyle, surface

## 실험에서 나타나지 않는 변화

| area | summary | evidence_notes | confidence |
| --- | --- | --- | --- |
| 알림·미리보기의 메시지 유형 구분 | 음성 메시지, 이미지, 영상, GIF, 설문, 스티커, 전달된 메시지와 여러 첨부 파일을 구분해 알리는 문구가 추가됐습니다. | Twelve strings provide per-message-type summaries such as sent a voice message, sent a poll, and forwarded a message. | high |
| Nitro 제휴 혜택 문구 정리 | Xbox Game Pass, Logitech·SteelSeries 할인, 추가 Orbs 혜택을 안내하던 대규모 문구 묶음이 클라이언트 데이터에서 삭제됐습니다. | Ninety English rows remove partner-benefit, claim, manage, eligibility, and discount copy in one extraction. | high |
| 게임 서버 호스팅 관리 | Shop에서 게임 서버를 찾는 흐름에 더해 갱신·해지일, Shop 보기, 서버 유지, 해지 뒤 데이터 삭제 안내가 추가됐습니다. | English and Korean copy covers Manage Game Servers, billing dates, cancellation, backups, uptime, DDoS protection, and Nitro discounts. | high |
| Nitro 체험·할인 가격 표시 | Nitro 체험 기간을 일·주·월·년 단위로 표시하고, 첫 할인 기간 뒤 정가와 월간 전용 조건을 설명하는 문구가 추가됐습니다. | New strings parameterize trial duration, first-month or first-year pricing, savings, and Monthly only eligibility. | high |
| 게임 계정 연결 안내 변경 | 외부 게임 계정 연결 안내가 단순 이전 공지에서 새로운 게임 내 소셜 기능을 위한 재연결 설명으로 바뀌었습니다. | Three strings now explain that relinking powers new in-game social features and can award Orbs. | high |
| 활동 접근성 안내 | 화면 읽기 사용자가 활동을 실행하고 빠져나오는 방법을 알 수 있도록 활동 이름과 제스처 설명이 추가됐습니다. | Accessibility copy names the activity and explains double tap plus the two-finger scrub exit gesture. | high |
| Shop 제안과 친구 장식 탐색 | 프로모션 적용 가능 여부와 ‘제안 사용’, ‘아이템 받기’ 동작이 추가되고, 친구가 쓰는 장식을 Shop에서 찾도록 돕는 문구가 다듬어졌습니다. | Offer eligibility, Use Offer, Get Item, View in Shop, and friend-decoration discovery copy changed together. | high |
| 게임 프로필 선호도와 검색 | 좋아하는 게임, 자주 하는 게임, 대표 게임을 프로필에 추가하는 분류와 자동 완성 결과에 게임을 표시하는 설정 문구가 추가됐습니다. | Strings add Games I Like, Games in Rotation, Favorite Game, Add Game, and Show games in autocomplete results. | high |
| LFG와 음성 화면 용어 정리 | 내장 음성이 포함된 새 LFG 경험 안내가 추가되고, 음성 화면 전환 문구가 ‘Living Room’과 ‘Grid View’처럼 더 짧은 이름으로 바뀌었습니다. | One LFG callout and two voice-view labels changed in the current window. | high |
| Clips 녹화 품질 설정 | Clips 설정에 녹화 품질과 파일 크기의 관계를 설명하는 새 항목이 추가됐습니다. | Clip Quality and a higher-quality/larger-file-size explanation were added together. | high |
| 프로필 메모 키보드 배치 | 프로필 메모를 화살표 키로 옮긴 뒤 Enter로 놓을 수 있다는 키보드 안내가 추가됐습니다. | A new instruction explicitly describes arrow-key positioning and Enter placement. | high |

## Unresolved 후보와 다음 확인 포인트

- 현재 unresolved 후보는 33개입니다. 이전 29개를 현재 번들과 이번 문자열 창에서 먼저 다시 확인했으며, 직접 소비가 새로 확인된 항목은 없었습니다.
- 이번 창에서 wishlist 직접 선물, 길드 프로필 서버 태그, Shop 게임 서버 호스팅, Powerups 코치마크 스크롤 종료 4개를 새 후보로 추가했습니다. 제품 화면 자체는 확인되지만 각 실험을 읽는 경로가 없어 public analysis는 비워 두었습니다.

| id | timestamp | status | reason | next_check_hint |
| --- | --- | --- | --- | --- |
| 2026-05-dvp-for-attachments | 2026-06-12T20:47:43Z | needs_evidence | no current experiment id or config consumer; attachment/viewer strings are still not enough to link the feature | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-remove-wishlist-dm-sidebar-side-copy | 2026-06-10T15:05:19Z | needs_evidence | no current experiment id, config consumer, or wishlist DM-sidebar copy surface found | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-bounty-use-video-modal-mobile-placement-experiment | 2026-06-13T03:48:57Z | needs_evidence | the definition remains unassigned near Quest/Bounties code and no mobile video-modal placement consumer was found | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-05-bounties-stage-1 | 2026-06-13T03:48:57Z | needs_evidence | the definition remains unassigned near Quest/Bounties code; timer, Orbs amount, scrolling, and looping keys still have no confirmed config consumer | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-quest-home-layout-visual-tweaks | 2026-07-07T23:29:41.973954+00:00 | needs_config_consumer | the definition and exported helper remain, but no current visible layout read was confirmed | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-server-setup-boost-cta | 2026-06-15T22:06:33Z | needs_evidence | server perk and Boost copy exists, but no current experiment id or config consumer links server setup to a Boost CTA | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-non-friend-messages-requests-in-uk | 2026-06-18T18:30:11Z | needs_evidence | no current experiment id or consumer ties UK users to a changed non-friend message-request path | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-clips-editor-v2 | 2026-06-22T21:21:29Z | needs_evidence | the current bundle still has no exact id or config consumer; new Clip Quality copy confirms a settings surface but does not link it to this experiment | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-mobile-server-tag | 2026-06-23T05:14:29Z | needs_evidence | the registration remains unassigned; the new guild-profile-server-tag row and server-tag copy do not establish this experiment's visible mobile consumer | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-polls-click-to-profile | 2026-06-26T19:09:12Z | needs_evidence | no current experiment id match or poll-click profile consumer found | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-game-invites-channel | 2026-06-26T21:06:12Z | needs_evidence | new built-in-voice LFG copy confirms a product surface, but no current exact id or config consumer links it to this experiment | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-similar-games-desktop | 2026-06-26T22:39:05Z | needs_evidence | new game-profile preference and autocomplete copy appeared, but no exact id or similar-games desktop consumer was found | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-similar-games-mobile | 2026-06-26T22:39:05Z | needs_evidence | new game-profile preference and autocomplete copy appeared, but no exact id or similar-games mobile consumer was found | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-server-boost-bar-nudge | 2026-06-30T19:02:56Z | needs_evidence | server perk and Boost copy exists, but no current experiment id or config consumer links the Boost bar nudge to a visible surface | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-improved-shop-loading | 2026-06-30T20:47:50Z | needs_evidence | no current experiment id or Shop loading consumer found | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-05-clips-timeline | 2026-06-30T18:26:23.440905+00:00 | needs_evidence | no current experiment id or Clips timeline consumer found in the current bundle | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-orb-redemptions-billing-history | 2026-06-30T01:03:49Z | needs_evidence | partner and Orbs benefit copy changed, but no exact id or billing-history config consumer links those strings to this experiment | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-game-profile-share-link | 2026-07-01T02:02:49.926027+00:00 | needs_ui_consumer | the current consumer still confirms coded-link analytics only; showSmallEmbed has no user-visible consumer | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-07-server-tag-game-profiles-desktop | 2026-07-06T17:01:20Z | needs_evidence | a new guild-profile-server-tag row and game-profile copy appeared, but no exact id or desktop server-tag consumer was confirmed | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-07-activity-entrypoint-ui | 2026-07-09T15:00:53Z | needs_evidence | new activity accessibility strings confirm an activity surface, but no exact id or activity-entrypoint config consumer was found | Look for an exact id match or a consumer tied to the activity panel entrypoint before writing public analysis. |
| 2026-07-smag-wishlist-recommendations-dismiss-threshold | 2026-07-09T22:37:43Z | needs_evidence | wishlist routes and a new direct-to-gifting row are present, but no exact id or dismissal-threshold consumer was found | Recheck wishlist recommendation modules for a dismissal counter or threshold config consumer. |
| 2026-07-smag-wishlist-nitro-first-slot | 2026-07-10T00:43:48Z | needs_evidence | wishlist routes and a new direct-to-gifting row are present, but no exact id or Nitro-first-slot consumer was found | Search current wishlist recommendation rendering for a Nitro-first-slot config read or visible placement consumer. |
| 2026-07-smag-dm-sidebar-nitro-recommendation | 2026-07-10T16:35:32Z | needs_evidence | wishlist routes and a new direct-to-gifting row are present, but no exact id or DM-sidebar Nitro recommendation consumer was found | Look for a DM sidebar recommendation component that reads this experiment or a matching config export. |
| 2026-07-shop-this-look | 2026-07-10T17:43:08Z | needs_evidence | friend-decoration discovery copy was refined, but the exact experiment id and config consumer remain absent | Re-search Shop/Collectibles chunks for a consumer that ties the string to the experiment before adding analysis. |
| 2026-07-quest-bar-secondary-cta | 2026-07-10T22:13:34Z | needs_evidence | the definition remains with showPlayInstantlyLabel, but no exported-symbol or component consumer was found | Find a Quest bar component that reads the exported experiment before writing user-facing analysis. |
| 2026-07-bounties-vertical-scroll | 2026-07-15T17:51:39Z | needs_config_consumer | vertical-scroll, affordance, auto-scroll, and peek settings are registered, but the registration result is not assigned or read | Find a Quest or Bounties component that reads the experiment result before writing public analysis. |
| 2026-07-collectibles-promotion-endpoint-reference | 2026-07-15T23:56:50Z | needs_experiment_linkage | new Promo, Use Offer, and offer-eligibility strings confirm a Shop offer flow, but no exact experiment or endpoint consumer links it to this row | Recheck Collectibles promotion-fetch code for this exact id or a returned offer object tied to a visible Shop surface. |
| 2026-06-wysiwyg-user-profile-premium-try-it-out | 2026-07-17T05:29:05Z | needs_experiment_linkage | Nitro profile-preview and Surprise Me strings confirm a visible try-it-out flow, but no exact experiment id or config consumer links that flow to this row | Find the WYSIWYG profile preview component and confirm that it reads this experiment before writing public analysis. |
| 2026-03-boost-to-unlock-mobile-coachmark | 2026-07-17T18:39:48.052938+00:00 | needs_ui_consumer | GuildPowerupsManager still reads showCoachmark only to decide whether mobile powerup data should be fetched; the new scroll-close coachmark row does not establish a visible consumer | Trace the mobile Boost coachmark component and confirm that the fetched powerup state plus this experiment controls its visibility. |
| 2026-07-wishlist-direct-to-gifting | 2026-07-21T16:05:07Z | needs_experiment_linkage | wishlist and gifting flows exist, but no exact experiment match or variant consumer links them to this row | Find a wishlist item or gifting action that reads this experiment and distinguishes Variant 1 from Variant 2 before writing public analysis. |
| 2026-06-guild-profile-server-tag | 2026-07-21T17:09:42Z | needs_experiment_linkage | server-tag state and profile copy exist, but no exact experiment match or config consumer connects this row to the visible guild profile | Trace guild-profile tag rendering to an exact experiment read or matching exported helper before writing public analysis. |
| 2026-06-game-server-hosting-in-shop | 2026-07-21T18:01:14Z | needs_experiment_linkage | Shop and game-server management copy confirm the product surface, but no exact experiment or treatment consumer was found | Find a Shop game-server card or route that reads this experiment and maps its three variants to visible placement behavior. |
| 2026-07-powerups-coachmark-scroll-close | 2026-07-21T23:35:16Z | needs_ui_consumer | Powerups coachmark code exists, but no exact experiment match or scroll-close consumer links that behavior to this row | Trace the visible Powerups coachmark close handler and confirm that scrolling reads this experiment before writing public analysis. |

## 검증 및 커밋/푸시 결과

- JSON 유효성: passed
- 리포트 구조: passed
- 금지 fallback 문구 검색: passed
- 공개 내용 점검: passed
- 최신 리포트 포인터 일치: passed
- git diff 검사: passed
- 커밋/푸시: passed (`f3f2c0b0ad` pushed to `origin/main`; metadata recorded by follow-up commit)
- 비고: No application or parser code changed, so code build checks are not required for this run.

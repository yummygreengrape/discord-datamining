# Discord 데이터마이닝 주간 리포트 — 2026-08-15

## 처리 기간과 빌드

- 처리 기간: `2026-08-12T04:01:50Z` ~ `2026-08-15T04:03:35Z`
- build_hash: `3aa8b0664700d6ddf09e26247056d258d54225d9`
- 근거 번들: `canary/web.24a25270ed756e7a.js`
- 입력 기준: ignored data/history.json을 우선 확인하고 current private extraction history 및 tracked data/web/*와 대조했습니다. public history에 빠진 실험 26행과 문자열 175행을 동기화했으며, latest_changes.json은 현재 빌드 확인을 위한 보조 신호로만 사용했습니다.

## 핵심 요약

- 실험 37행 / 30개 ID, API 0행, 문자열 221행(197개 고유 행)을 검토했습니다.
- disposition은 interpreted 9행, strengthened_existing 5행, deleted_preserved_context 4행, unresolved_needs_evidence 2행, internal_or_low_value 1행, deletion_only_no_context 16행입니다.
- 예약 메시지, 지역별 영상·화면 공유 제한, 게임 서버 호스팅 활동 패널, Rich Presence 초대 배너, 프로필 링크 미리보기, 첨부 이미지 해상도 최적화를 실제 소비 경로 근거로 해석했습니다.
- 이전 unresolved의 2026-06-game-server-hosting-in-shop은 현재 활동 패널 소비를 확인해 승격했고, 삭제된 collectibles-promotion-endpoint-reference는 해석 없이 정리했습니다.
- premium-gifting-gogo-promotion과 profile-embed-share-button은 각각 실제 호출부와 정확한 실험 연결이 부족해 새 unresolved로 남겼습니다.
- raw 갱신 전 175개 Codex 해석이 모두 보존돼 별도 복구는 필요하지 않았고, 이번 반영 뒤 history/web parity 기준 해석은 194행입니다.

## 실험 전수 분석 결과

### interpreted

| ID | 시각 | 상태 | 판단 | 근거 |
|---|---|---|---|---|
| `2026-07-attachment-image-ladder` | `2026-08-14T18:57:36.913267+00:00` | modified | interpreted | ImageLoaderUtils now reads the config and applies a bounded resolution ladder to attachment requests |
| `2026-08-rich-presence-invite-banner` | `2026-08-14T14:52:15Z` | added | interpreted | the channel composer reads showBanner and renders a send-invite banner for a joinable activity |
| `2026-08-profile-embed-rendering` | `2026-08-14T12:56:24Z` | added | interpreted | message markup post-processing reads the experiment and removes duplicate raw profile links from link-only embed messages |
| `2026-08-video-guard` | `2026-08-14T00:43:01Z` | added | interpreted | camera, screen-share, and connected-call paths read videoEnabled and use regional restriction UI when false |
| `2026-08-scheduled-messages` | `2026-08-14T00:21:50Z` | added | interpreted | the composer and schedule command use the enabled gate and connect to create, fetch, update, and delete actions |
| `2026-08-bounties-mobile-quest-bar` | `2026-08-13T15:09:44Z` | added | interpreted | QuestActionCreators reads the gate before admitting BOUNTY creatives from the Quest decision response |
| `2026-08-gsh-subs-activity-bar` | `2026-08-12T20:54:24Z` | added | interpreted | the activity-panel hosting button reads the experiment to enable its coachmark and new-badge candidates |
| `2026-08-gsh-subs-activity-bar` | `2026-08-12T20:48:19Z` | added | interpreted | the activity-panel hosting button reads the experiment to enable its coachmark and new-badge candidates |
| `2026-06-minimal-detectable` | `2026-08-12T16:10:47Z` | added | interpreted | game and non-game detection fetchers read the experiment and switch to v1 list files |

### strengthened

| ID | 시각 | 상태 | 판단 | 근거 |
|---|---|---|---|---|
| `2026-06-battlenet-social-sdk-migration` | `2026-08-14T21:15:13.899986+00:00` | modified | strengthened_existing | the current Battle.net app-account mapping still reads the same enabled migration gate |
| `2026-06-battlenet-social-sdk-migration` | `2026-08-14T21:06:32Z` | modified | strengthened_existing | the current Battle.net app-account mapping still reads the same enabled migration gate |
| `2026-08-scheduled-messages` | `2026-08-14T00:33:19.704187+00:00` | modified | strengthened_existing | the current route/action/store flow confirms creation, fetching, editing, and deletion while the modified row drops treatment labels |
| `2026-07-expressive-modal-v2` | `2026-08-13T22:26:32.740905+00:00` | modified | strengthened_existing | the current age-verification entry point still reads the experiment and both variants now carry the same enabled value |
| `2026-07-nvenc-reconstructed-frames` | `2026-08-12T22:42:18Z` | added | strengthened_existing | the current media setup again reads the experiment and appends the NVIDIA reconstructed-frames option |

### deleted context preserved

| ID | 시각 | 상태 | 판단 | 근거 |
|---|---|---|---|---|
| `2026-06_guild_rooms` | `2026-08-13T20:49:54Z` | deleted | deleted_preserved_context | prior behavior-linked Living Room and seat-flow context is preserved without inferring rollout or rollback |
| `2026-06-pix-for-otp` | `2026-08-12T22:55:27Z` | deleted | deleted_preserved_context | prior behavior-linked Pix checkout context is preserved without inferring rollout or rollback |
| `2026-08-gsh-subs-activity-bar` | `2026-08-12T20:52:22Z` | deleted | deleted_preserved_context | same-window behavior-linked hosting-promotion context is preserved without inferring rollout or rollback |
| `2026-06-friendship-anniversary-backend-persistence` | `2026-08-12T17:09:12.825800+00:00` | deleted | deleted_preserved_context | prior behavior-linked cross-device dismissal synchronization context is preserved without inferring rollout or rollback |

### unresolved

| ID | 시각 | 상태 | 판단 | 근거 |
|---|---|---|---|---|
| `2026-08-profile-embed-share-button` | `2026-08-14T17:11:24Z` | added | unresolved_needs_evidence | Share Profile copy and profile-send code exist, but no exact experiment id or config consumer links the button to this row |
| `2026-08-premium-gifting-gogo-promotion` | `2026-08-13T22:36:53Z` | added | unresolved_needs_evidence | the experiment is read by an exported free-SKU-step helper, but no current module calls that helper |

### internal or low value

| ID | 시각 | 상태 | 판단 | 근거 |
|---|---|---|---|---|
| `2026-02-client-heartbeat-skipped` | `2026-08-13T17:36:01Z` | added | internal_or_low_value | the row only controls skipped-heartbeat logging and disappeared again within minutes |

### deletion-only

| ID | 시각 | 상태 | 판단 | 근거 |
|---|---|---|---|---|
| `2026-04-profile-frame-gifting` | `2026-08-14T23:33:52Z` | deleted | deletion_only_no_context | no prior evidence-backed interpretation or current exact consumer was available |
| `2026-07-collectibles-promotion-endpoint-reference` | `2026-08-14T22:04:01Z` | deleted | deletion_only_no_context | the prior unresolved row was deleted without ever gaining a behavior-linked consumer |
| `2026-05-valorant-social-sdk-us--canada` | `2026-08-14T21:15:13.899986+00:00` | deleted | deletion_only_no_context | no prior evidence-backed interpretation or current exact experiment consumer was available |
| `2026-05-valorant-social-sdk-all-regions` | `2026-08-14T21:15:13.899986+00:00` | deleted | deletion_only_no_context | no prior evidence-backed interpretation or current exact experiment consumer was available |
| `2026-05-riot-social-sdk-migration-us--canada` | `2026-08-14T21:15:13.899986+00:00` | deleted | deletion_only_no_context | no prior evidence-backed interpretation or current exact experiment consumer was available |
| `2026-05-riot-social-sdk-migration-all-regions` | `2026-08-14T21:15:13.899986+00:00` | deleted | deletion_only_no_context | no prior evidence-backed interpretation or current exact experiment consumer was available |
| `2026-04-valorant-social-sdk` | `2026-08-14T21:15:13.899986+00:00` | deleted | deletion_only_no_context | no prior evidence-backed interpretation or current exact experiment consumer was available |
| `2026-04-riot-social-sdk-migration` | `2026-08-14T21:15:13.899986+00:00` | deleted | deletion_only_no_context | no prior evidence-backed interpretation or current exact experiment consumer was available |
| `2026-04-scheduled-messages-ui-backup` | `2026-08-14T00:21:50Z` | deleted | deletion_only_no_context | no prior evidence-backed interpretation or current exact consumer was available |
| `2026-02-client-heartbeat-skipped` | `2026-08-13T17:39:04Z` | deleted | deletion_only_no_context | the telemetry-only row was deleted and has no supported user-facing context to preserve |
| `2026-02-client-heartbeat-skipped` | `2026-08-13T17:30:58Z` | deleted | deletion_only_no_context | the telemetry-only row has no supported user-facing context to preserve |
| `2026-02-client-heartbeat-skipped` | `2026-08-13T17:30:33.579364+00:00` | deleted | deletion_only_no_context | the raw config only concerns skipped-heartbeat logging and has no user-facing interpretation |
| `2025-10-ad-request-behavior-experiment` | `2026-08-12T19:53:47Z` | deleted | deletion_only_no_context | no prior evidence-backed interpretation or current exact consumer was available |
| `2026-05-user-settings-redesign-4d` | `2026-08-12T18:25:00Z` | deleted | deletion_only_no_context | no prior evidence-backed interpretation or current exact consumer was available |
| `2025-10-friendship-anniversary-gifting` | `2026-08-12T17:57:45Z` | deleted | deletion_only_no_context | no prior evidence-backed interpretation or current exact consumer was available |
| `2026-03-boosting-settings-refresh` | `2026-08-12T13:41:34Z` | deleted | deletion_only_no_context | no prior evidence-backed interpretation or current exact consumer was available |

## 중요한 실험 상세 해석

### 예약 메시지 작성·관리 (`2026-08-scheduled-messages`)

메시지를 미래 시각에 보내도록 예약하고, 예약 내역을 수정하거나 삭제할 수 있게 하는 실험입니다.

- 근거: The composer gate, schedule command, store, and create/fetch/update/delete actions form a complete current consumer path.
- 확인 단서: Schedule Message, future send time, edit, delete, attachments

### 지역별 영상·화면 공유 제한 (`2026-08-video-guard`)

지역 제한이 적용될 때 카메라와 화면 공유를 차단하고 이유를 안내하는 실험입니다.

- 근거: Camera, screen-share, and connected-call paths read videoEnabled; current copy names a Brazilian government order.
- 확인 단서: videoEnabled=false, VideoGuardBannerManager, Brazilian government order

### 활동 패널 게임 서버 호스팅 (`2026-06-game-server-hosting-in-shop`)

지원 게임을 실행 중일 때 활동 패널에서 해당 게임의 서버 호스팅 요금제를 열 수 있게 합니다.

- 근거: The current activity panel calls the experiment helper and opens the Game Servers Shop tab for the running game.
- 확인 단서: activity-panel, Game Servers Shop, running game, personalization consent

### 호스팅 버튼 홍보 배지 (`2026-08-gsh-subs-activity-bar`)

게임 서버 호스팅 버튼에 새 배지와 요금제 안내 코치마크를 붙이는 실험입니다.

- 근거: The activity-panel component passes the config as marketingEnabled for the hosted-server badge and coachmark.
- 확인 단서: Host a {gameName} game server, View plans, marketingEnabled

### 채팅창 게임 초대 배너 (`2026-08-rich-presence-invite-banner`)

함께 플레이할 수 있는 활동이 있을 때 채팅 입력창 위에서 채널 초대를 바로 보냅니다.

- 근거: The ChannelTextAreaBars consumer renders the activity name, invite action, and dismissal state.
- 확인 단서: Invite to Play, ChannelTextAreaBars, sendActivityInvite

### 프로필 링크 미리보기 정리 (`2026-08-profile-embed-rendering`)

프로필 링크만 보낸 메시지에서 원본 URL을 중복 표시하지 않고 미리보기에 집중합니다.

- 근거: Markup post-processing filters /users/:id link nodes only for profile-link-only messages.
- 확인 단서: /users/:id, MarkupPostProcessors, profile embed

### 첨부 이미지 해상도 최적화 (`2026-07-attachment-image-ladder`)

화면 크기에 가까운 단계형 해상도를 골라 첨부 이미지 다운로드 크기를 줄이는 실험입니다.

- 근거: ImageLoaderUtils reads maxUpscale and minSnapDownDpr before selecting an attachment image bucket.
- 확인 단서: maxUpscale=1.1, minSnapDownDpr=2, 128-4096 ladder

### Quest bar Bounty 표시 (`2026-08-bounties-mobile-quest-bar`)

Quest 전달 응답의 Bounty 형식을 버리지 않고 Quest bar 상태로 전달합니다.

- 근거: QuestActionCreators filters BOUNTY creatives on this config before dispatch.
- 확인 단서: QUEST_FETCH_QUEST_TO_DELIVER, BOUNTY, Quest bar state

### 새 게임·앱 감지 목록 (`2026-06-minimal-detectable`)

실행 중인 게임과 비게임 앱을 인식할 때 새 v1 감지 목록을 사용합니다.

- 근거: Both game and non-game fetchers switch to v1 list files; content differences remain unknown.
- 확인 단서: games-v1.json, non-games-v1.json, activity detection

## 실험에서 나타나지 않는 변화

- 이번 처리 창의 API endpoint 변경 행은 0개였습니다.

| 영역 | 제품 변화 | 근거와 확신도 |
|---|---|---|
| 프로필 배지 공개 범위·순서 | 프로필에 공개하고 싶지 않은 배지를 숨기고, Nitro로 배지 순서를 바꾸는 안내와 드래그·접근성 문구가 추가됐습니다. | A coherent badge cluster covers visibility toggles, drag reorder, Nitro gating, and screen-reader position changes. (high) |
| 연령 제한 서버 확인 | 지역 연령 기준 때문에 서버 접근이 제한될 때 나이를 확인하거나 잘못된 판정을 다시 확인하는 흐름이 추가됐습니다. | New strings include Age-Restricted Server, Confirm Age, a pre-join prompt, and a reconfirmation path. (high) |
| 브라질 영상·화면 공유 제한 안내 | 영상과 화면 공유가 브라질 정부 명령으로 제한된다는 구체적인 안내 문구가 추가됐습니다. | Generic regional-unavailable copy is replaced with explicit Brazilian government-order wording. (high) |
| 예약 메시지 사용자 흐름 | 예약 날짜와 시각을 확인하는 문구가 다듬어졌고, 현재 클라이언트에는 작성·목록·수정·삭제 흐름이 함께 연결돼 있습니다. | Scheduling confirmation copy changed in the window while current actions cover the full lifecycle. (high) |
| 게임 서버 호스팅 활동 패널 | 실행 중인 게임에서 호스팅 서버를 만들고 요금제를 보는 활동 패널 안내가 추가됐습니다. | Strings and current component code align on a hosted-server button, coachmark, and Shop destination. (high) |
| Rich Presence 채널 초대 | 현재 채널 사람들을 게임에 초대하는 입력창 배너와 닫은 뒤 더하기 버튼을 안내하는 문구가 추가됐습니다. | The invite-banner component and three same-window strings describe one coherent flow. (high) |
| 프로필 공유·미리보기 | Share Profile 동작과 프로필 링크 미리보기 정리가 함께 나타났습니다. 공유 버튼 실험의 정확한 노출 조건은 아직 확인되지 않았습니다. | Profile-send code and Share Profile copy are present, while only the separate rendering experiment has a confirmed config consumer. (medium) |
| 후원 콘텐츠 주제 제어 | 후원 콘텐츠 개인화와 표시 주제를 관리하고 Real Money Gaming 같은 주제를 숨길 수 있는 설정 문구가 추가됐습니다. | A complete preference cluster includes shown/hidden states, topics, policy guidance, and management actions. (high) |
| 앱 영역 캡처·파일 첨부 | 앱의 특정 영역을 캡처해 파일로 붙이고, 크기·개수·누락 오류를 처리하는 흐름이 문자열로 구체화됐습니다. | A same-time cluster covers Capture Region, Attach Files, downloads, unavailable files, and size/count failures. (high) |
| 성능 추적 캡처 | 30초 동안 성능 정보를 기록해 Downloads 폴더에 저장하고 지원 문의에 첨부하는 진단 흐름이 추가됐습니다. | Six strings cover starting, progress, completion, duration, storage location, and support-ticket use. (high) |
| 선물 구매 5,000 Orbs 보상 | 특정 선물 구매를 완료하면 5,000 Orbs를 받고 Shop에서 쓸 수 있다는 보상 안내가 추가됐습니다. | Purchase-condition, reward, unlock, and Shop-spend strings form one flow. (high) |
| Living Room 보기 기억·상태 활동 | 음성 채널 재입장 시 Living Room 또는 Grid의 마지막 보기를 기억하는 설정과 사용자 메모·상태 활동 문구가 추가됐습니다. | Remember my last view appears with note, posture, and cleared-state activity strings. (high) |
| Server Hub 패널 관리 | Server Hub 편집 명칭이 구체화되고 활성 패널 수를 보여 주는 문구가 추가됐습니다. | Edit Hub is replaced by Edit Server Hub and a panel-count label appears. (high) |
| 채널 생성 감사 로그 | 미디어·포럼·공지 채널이 만들어졌을 때 생성자와 대상 채널을 표시하는 감사 로그 문구가 추가됐습니다. | Three parallel audit-log strings cover media, forum, and announcement channel creation. (high) |
| 프로필 배너·GIF 편집 | 프로필 배너를 편집하거나 제거하고 GIF 애니메이션 여부를 고르는 편집 동작이 추가됐습니다. | Edit Banner, Remove banner, and Animate GIF arrive in the same profile-editing window. (medium) |

## unresolved 후보와 다음 확인 포인트

| ID | 보류 이유 | 다음 확인 |
|---|---|---|
| `2026-05-dvp-for-attachments` | no current experiment id or config consumer; attachment/viewer strings are still not enough to link the feature | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-05-bounties-stage-1` | the current bundle still registers timer, Orbs, looping, and scroll settings without assigning or reading the experiment result | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-06-server-setup-boost-cta` | server perk and Boost copy exists, but no current experiment id or config consumer links server setup to a Boost CTA | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-06-non-friend-messages-requests-in-uk` | no current experiment id or consumer ties UK users to a changed non-friend message-request path | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-06-clips-editor-v2` | new Auto Clips settings copy confirms active Clips work, but no current exact id or editor-v2 config consumer links that surface to this experiment | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-06-mobile-server-tag` | the current guild profile/store module still registers the experiment without assigning or reading the returned config | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-06-game-invites-channel` | new built-in-voice LFG copy confirms a product surface, but no current exact id or config consumer links it to this experiment | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-06-similar-games-desktop` | new game media and rating labels strengthen a game-profile surface, but no exact id or similar-games desktop consumer was found | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-06-similar-games-mobile` | new game media and rating labels strengthen a game-profile surface, but no exact id or similar-games mobile consumer was found | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-06-orb-redemptions-billing-history` | partner and Orbs benefit copy changed, but no exact id or billing-history config consumer links those strings to this experiment | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-05-clips-timeline` | no current experiment id or Clips timeline consumer found in the current bundle | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-06-improved-shop-loading` | no current experiment id or Shop loading consumer found | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-07-server-tag-game-profiles-desktop` | a new guild-profile-server-tag row and game-profile copy appeared, but no exact id or desktop server-tag consumer was confirmed | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-06-quest-home-layout-visual-tweaks` | the current Quest module exports the experiment, but no current import site reads the exported config object | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-07-smag-wishlist-recommendations-dismiss-threshold` | wishlist routes and a new direct-to-gifting row are present, but no exact id or dismissal-threshold consumer was found | Recheck wishlist recommendation modules for a dismissal counter or threshold config consumer. |
| `2026-07-smag-wishlist-nitro-first-slot` | wishlist routes and a new direct-to-gifting row are present, but no exact id or Nitro-first-slot consumer was found | Search current wishlist recommendation rendering for a Nitro-first-slot config read or visible placement consumer. |
| `2026-07-smag-dm-sidebar-nitro-recommendation` | wishlist routes and a new direct-to-gifting row are present, but no exact id or DM-sidebar Nitro recommendation consumer was found | Look for a DM sidebar recommendation component that reads this experiment or a matching config export. |
| `2026-07-shop-this-look` | Shop This Look and an item-unavailable purchase state are visible, but no exact experiment id or config consumer links that surface to this row | Trace the Shop this Look dismissible content to an exact experiment read before adding public analysis. |
| `2026-07-quest-bar-secondary-cta` | showPlayInstantlyLabel remains defined, but no Quest bar component reads the experiment | Find a Quest bar component that reads the exported experiment before writing user-facing analysis. |
| `2026-07-bounties-vertical-scroll` | vertical-scroll and auto-scroll settings remain registered, but the returned experiment object is not assigned or consumed | Find a Quest or Bounties component that reads the experiment result before writing public analysis. |
| `2026-06-wysiwyg-user-profile-premium-try-it-out` | new Personal Widget Try it Out copy confirms a profile upsell surface, but no exact id or config consumer links that separate flow to this experiment | Find the profile try-out renderer and confirm that it reads this experiment before writing public analysis. |
| `2026-03-boost-to-unlock-mobile-coachmark` | the mobile GuildPowerupsManager reads showCoachmark only to decide whether Powerups data should be fetched; no visible coachmark renderer is linked to the result | Trace the mobile Powerups coachmark renderer and confirm that the fetched data plus this experiment controls visible exposure before writing public analysis. |
| `2026-07-wishlist-direct-to-gifting` | wishlist and gifting flows exist, but no exact experiment match or variant consumer links them to this row | Find a wishlist item or gifting action that reads this experiment and distinguishes Variant 1 from Variant 2 before writing public analysis. |
| `2026-06-guild-profile-server-tag` | server-tag state and profile copy exist, but no exact experiment match or config consumer connects this row to the visible guild profile | Trace guild-profile tag rendering to an exact experiment read or matching exported helper before writing public analysis. |
| `2026-07-powerups-coachmark-scroll-close` | Powerups coachmark code exists, but no exact experiment match or scroll-close consumer links that behavior to this row | Trace the visible Powerups coachmark close handler and confirm that scrolling reads this experiment before writing public analysis. |
| `2026-07-collectibles-collabs-filter` | Collabs, Collabs counts, and Offer Eligible counts confirm a Shop filter surface, but no exact experiment id or filter consumer was found | Trace the Shop filter rendering and confirm an exact experiment read before adding public analysis. |
| `2026-05-quest-home-tile-redesign` | the current definition exports layout and clickable-tile options, but no current Quest Home component reads the exported experiment object | Find a Quest Home tile or layout component that reads the exported experiment object before writing public analysis. |
| `2026-07-nitro-home-header-followup` | Nitro Home and free Shop-item strings changed, but no exact experiment id or header variant consumer was found | Trace the Nitro Home header component and confirm how Variant 0 and Variant 1 change the visible header. |
| `2026-06-hero-shelf-ad-tile` | the row suggests a visible advertising tile, but no exact experiment id, shelf component, route, or treatment consumer was found | Find a rendered shelf or advertising card that reads this experiment before writing public analysis. |
| `2026-07-gdop-discovery` | no exact experiment id, config consumer, route, or visible discovery component was found | Find an exact experiment registration or discovery component that distinguishes Variant 0 from Variant 1. |
| `2026-07-social-layer-storefront-spend-orbs-banner-copy` | time-limited Nitro and Orbs item copy confirms a storefront banner surface, but no exact experiment id or variant consumer links that copy to this row | Trace the social-layer storefront banner renderer to an exact experiment read and compare the two copy variants. |
| `2026-07-call-of-duty-3pp-expired` | the exact experiment exposes a useConfig helper, but the current Nitro tab calls only the two marketing helpers and no expired-state component calls this helper | Find an expired-state component that directly reads this experiment before adding public analysis. |
| `2026-07-cod-3pp` | the exact experiment exposes a useConfig helper, but no current caller uses the base Call of Duty helper; only the two sibling marketing helpers are called by the Nitro tab | Find a Call of Duty provider or reward entrypoint that calls the base experiment helper before writing public analysis. |
| `2026-07-wishlist-show-owned-items-last` | wishlist and gifting surfaces exist, but no exact experiment id or owned-item sorting consumer was found | Find the wishlist item sorter and confirm that it reads this experiment before moving owned items to the end. |
| `2026-08-soundboard-desktop-nux` | the current strings now include the desktop Soundboard introduction in Korean, but no exact experiment id or config read ties the NUX exposure to this row | Trace the Soundboard NUX renderer to an exact experiment read before adding public analysis. |
| `2026-07-game-mentions-v2-mobile` | the exact mobile experiment remains registration-only; its returned config is not assigned or read by the mobile autocomplete path | Find the mobile game-mention autocomplete component that reads this experiment before writing public analysis. |
| `2026-07-clips-editor-text-track` | Clips now has title and text-or-image editing copy, but no exact experiment id, config object, or text-track consumer links those controls to this row | Find a Clips editor text or caption track component tied to this experiment before writing public analysis. |
| `2026-07-plan-select-ui-redesign` | yearly-switch copy was deleted in the same window, but no current exact experiment id or plan-selection variant consumer was found | Find a plan-selection screen that reads this experiment and compare Variant 0 with Variant 1 before writing public analysis. |
| `2026-08-hide-gift-shop-upsell` | gift and Shop purchase surfaces remain present, but no current exact experiment id or consumer that hides the upsell was found | Trace the gifting checkout or Shop upsell renderer to an exact experiment read before describing what is hidden. |
| `2026-07-custom-app-store-overlay` | the exact experiment is registered beside the app-store overlay feature gate, but its returned config is not assigned, exported, or read by a visible overlay surface | Find an overlay component that reads this exact experiment before describing how the custom app-store overlay differs from the existing feature gate. |
| `2026-08-premium-gifting-gogo-promotion` | the exact experiment is read by an exported free-SKU-step helper, but no current module calls that helper; active imports use unrelated gradient and reminder helpers | Find a gifting checkout component that calls the free-SKU-step helper and confirm how the enabled path changes selection before writing public analysis. |
| `2026-08-profile-embed-share-button` | Share Profile copy and app-directory profile sending code exist, but the exact experiment id and a config consumer are absent from the current bundle | Trace the Share Profile button renderer to an exact experiment read before describing its visibility or placement. |

## 검증 및 커밋/푸시 결과

- json_validity: passed
- report_shape: passed
- history_public_parity: passed (194 rows)
- paired_language_analysis: passed
- unresolved_required_fields: passed (42 candidates)
- forbidden_fallback_phrase_search: passed
- tracked_public_content_check: passed (scoped public paths; reviewed product-metadata allowlist only)
- report_pointer_equality: passed
- repository_tests: passed (12 tests)
- git_diff_check: passed
- notes: JSON and report contracts, 194-row history/public interpretation parity, bilingual pairing and English purity, 42 unresolved records, fallback phrases, report pointers, 12 repository tests, scoped public-path security scanning, and git diff checks passed. The required full-checkout scan reported only the intentionally ignored local data/history.json and pre-existing .DS_Store files; none is staged or published. No parser or application code changed.
- data_commit: e66d998b44a6076322d3c8fea97a73dfc98b888c
- report_publish_commit: recorded by this follow-up metadata commit
- pushed: true
- publish_status: passed (e66d998b44a6 pushed to origin/main; final metadata recorded by follow-up commit)

## Security/privacy impact

No trust boundary, collection, transmission, retention, deletion, backup, access-control, or public schema changed. This run publishes only public Discord product metadata interpretations and aggregate evidence notes; it adds no user identifiers, message contents, credentials, private runner state, or private parser logic.

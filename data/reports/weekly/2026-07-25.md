# Discord Datamining Weekly Report - 2026-07-25

- 처리 기간: `2026-07-22T04:03:13Z` - `2026-07-25T04:02:14Z`
- 실행 시각: `2026-07-25 13:02:14 KST`
- build_hash: `a6d9d72723900a7ea5468618c0e957227616301b`
- 근거 번들: `canary/web.5c00f58942db4071.js`
- 입력 기준: `data/history.json`을 우선 확인하고 tracked `data/web/*`와 대조했습니다. local history에서 빠진 실험 2개와 문자열 34개를 복구하고 raw detail이 어긋난 실험 4행을 tracked web 기준으로 동기화했으며, `latest_changes.json`은 현재 빌드의 빈 보조 신호로만 확인했습니다.

## 핵심 요약

- 이번 처리 창에는 실험 30행(24개 ID), API 8행, 문자열 296행이 있습니다. 실제 소비가 확인된 7행을 새로 해석하고 기존 해석 4행을 현재 수정 내용에 맞게 보강했습니다.
- Favorites의 제한적 무료 접근, Guild Space, Nitro 연체 결제, 새 연령 확인 모달, 서버용 Magic Builder, NVIDIA 영상 인코딩 옵션이 현재 Canary 소비 코드로 확인됐습니다.
- 기존 Guild Rooms는 상호작용·여러 방·자세 비교안으로 세분화됐고, Consistent Profiles는 확인되지 않았던 두 번째 비교안을 제거한 현재 범위로 정리했습니다.
- 근거 있는 과거 해석 3개는 삭제 행에 맥락을 보존했지만 배포 또는 철회로 단정하지 않았습니다. 정의만 남은 2행은 unresolved, 보존 맥락 없는 삭제 10행은 deletion-only로 분류했습니다.
- 실험 외 변화는 Magic Builder, 게임 서버 생성·요금제·해지, 리마인더 분리, 연령 확인 방식 v2, 주문 취소 서명, 프로필 프리셋, 음성 연결 용어, Collectibles 필터가 중심입니다.

## 실험 전수 분석 결과

### interpreted

| id | timestamp | status | reason | evidence_notes |
| --- | --- | --- | --- | --- |
| 2026-07-past-due-checkout | 2026-07-24T19:06:32.624254+00:00 | modified | the current subscription notice reads enabled and routes past-due users to an open-invoice checkout | The consumer checks PAST_DUE status, loads the open invoice, disables while loading, and opens checkout when ready. |
| 2026-07-nvenc-reconstructed-frames | 2026-07-23T20:21:29Z | added | the media engine reads the flag while building its video encoder option list | The enabled branch adds nvReconFrames; no user-facing switch or measured performance direction is claimed. |
| 2026-07-vibegrations-guild | 2026-07-23T17:12:25.712660+00:00 | added | the guild experiment is read by the app-builder surface together with Manage Guild and Manage Channels permission | Current strings cover creation, previews, builds, bot permissions, publishing, production, and deletion. |
| 2026-07-expressive-modal-v2 | 2026-07-23T04:13:30Z | added | the age-verification start path reads the flag and selects a distinct modal | Dedicated Incode and Google Wallet paths remain separate; the general enabled path opens the new modal. |
| 2026-01-favorites-server | 2026-07-22T22:14:18.389344+00:00 | modified | current Favorites access and onboarding consumers read the newly added freemium variant | The freemium path allows access with a limit of three favorites; Nitro users retain the existing limit. |
| 2026-07-past-due-checkout | 2026-07-22T16:58:52Z | added | the current subscription notice reads enabled and routes past-due users to an open-invoice checkout | The banner style value is registered but not consumed by the confirmed notice path. |
| 2026-06_guild_spaces | 2026-07-22T16:56:50Z | added | channel rendering and route access read the guild experiment together with Manage Guild permission | The GUILD_SPACE route is exposed only when the experiment and permission checks pass; Server Hub copy appeared at the same time. |

### strengthened_existing

| id | timestamp | status | reason | evidence_notes |
| --- | --- | --- | --- | --- |
| 2026-06_guild_rooms | 2026-07-23T20:40:26.994036+00:00 | modified | the final treatment set adds the no-postures comparison while current room and interaction consumers remain active | enabled still drives room UI and seat connections; interactionsEnabled still gates room-positioned voice, while postures has no confirmed consumer. |
| 2026-04-consistent-profiles | 2026-07-23T19:06:45.754114+00:00 | modified | the current row removes the unconfirmed second treatment while current member-list and activity-header consumers remain | PeopleUserInfo and NowPlayingHeader both read enabled for consistent guild-tag and avatar-decoration rendering. |
| 2026-06_guild_rooms | 2026-07-23T18:04:23.926165+00:00 | modified | the treatment list adds room variants to the existing evidence-backed Living Room experiment | Room UI and interactions remain confirmed; multipleRoomsEnabled is registered but not consumed in the current bundle. |
| 2026-06_guild_rooms | 2026-07-23T16:10:15.431591+00:00 | modified | the treatment list adds a no-interactions comparison to the existing evidence-backed Living Room experiment | Current room UI and seat consumers read enabled, and room-positioned voice reads interactionsEnabled. |

### deleted_preserved_context

| id | timestamp | status | reason | evidence_notes |
| --- | --- | --- | --- | --- |
| 2026-06-expressive-button-test | 2026-07-23T22:00:31Z | deleted | a prior evidence-backed picker-upsell interpretation is preserved on the deletion row | Earlier Canary code read the button style in emoji and soundboard Nitro upsells; deletion alone does not establish rollback. |
| 2026-06-emoji-frecent-test | 2026-07-23T22:00:31Z | deleted | a prior evidence-backed frequent-emoji interpretation is preserved on the deletion row | Earlier Canary code capped the frequent emoji section at 9 or 18; deletion alone does not establish rollback. |
| 2026-06-application-widget-profile-popout-preload | 2026-07-22T18:12:30Z | deleted | a prior evidence-backed profile-card preload interpretation is preserved on the deletion row | Earlier Canary code preloaded widget, activity, image, and profile data from the popout hover path; deletion does not prove rollback. |

### unresolved_needs_evidence

| id | timestamp | status | reason | evidence_notes |
| --- | --- | --- | --- | --- |
| 2026-05-quest-home-tile-redesign | 2026-07-22T23:47:28.283974+00:00 | modified | the exported definition adds a clickable-tile treatment, but no current import reads the experiment object | Module 192444 exports the registration as aD; current import sites do not use aD. |
| 2026-07-collectibles-collabs-filter | 2026-07-22T18:21:37Z | added | Collabs and count strings confirm a Shop filter surface, but no exact experiment or filter consumer was found | Collabs, Collabs ({count}), and Offer Eligible ({count}) are product evidence without experiment linkage. |

### internal_or_low_value

| id | timestamp | status | reason | evidence_notes |
| --- | --- | --- | --- | --- |
| 2026-07-desktop-tti-update-backoff-algo | 2026-07-24T20:58:49Z | added | the config is consumed only by the desktop update manager and has no user-facing surface | The enabled algorithm value is synchronized to a native desktop setting after connection open. |

### no_current_surface

| id | timestamp | status | reason | evidence_notes |
| --- | --- | --- | --- | --- |
| 2026-06-expressive-button-test | 2026-07-23T22:02:33Z | added | the reference row reappeared two minutes after deletion, but the current bundle has no exact id or picker consumer | Prior behavior remains documented on the deletion row; no analysis was copied to this unsupported re-add row. |
| 2026-06-emoji-frecent-test | 2026-07-23T22:02:33Z | added | the reference row reappeared two minutes after deletion, but the current bundle has no exact id or grid consumer | Prior behavior remains documented on the deletion row; no analysis was copied to this unsupported re-add row. |
| 2026-07-game-mentions-v2-mobile | 2026-07-23T16:37:28Z | added | the row defines mobile mention options but was deleted later the same day and has no current exact id or consumer | Treatment names alone are insufficient to attach public analysis. |

### deletion_only_no_context

| id | timestamp | status | reason | evidence_notes |
| --- | --- | --- | --- | --- |
| 2026-05-orbs-purchase-upsell-banner | 2026-07-23T22:49:59Z | deleted | deleted without a prior evidence-backed interpretation or current experiment consumer | Monthly Orbs upsell copy was removed nearby, but that does not prove this experiment's rollout state. |
| 2026-05-orbs-shop-upsell-banner | 2026-07-23T22:49:59Z | deleted | deleted without a prior evidence-backed interpretation or current experiment consumer | Shop Orbs copy was removed nearby, but no current exact id or behavior-linked consumer remains. |
| 2026-06-bounty-use-video-modal-mobile-placement-experiment | 2026-07-23T20:08:21Z | deleted | deleted after remaining unresolved, with no prior public interpretation or current consumer to preserve | The candidate is removed from unresolved; deletion is not treated as rollout or rollback. |
| 2026-07-game-mentions-v2-mobile | 2026-07-23T19:01:47Z | deleted | deleted without a prior evidence-backed interpretation or current mobile consumer | New-badge strings nearby do not establish the game-mention surface or treatment behavior. |
| 2026-06-notify-friends-on-profile-update | 2026-07-23T16:33:24Z | deleted | deleted without a prior interpretation or a current profile-update notification consumer | No exact id, related action, or user-facing notification path remains in current Canary. |
| 2026-03-mac-new-updater | 2026-07-23T15:59:48.877517+00:00 | deleted | deleted without a prior public interpretation or current macOS updater consumer | No current exact id or user-facing updater setting remains. |
| 2026-01-valentines-day-drop | 2026-07-22T22:51:07Z | deleted | deleted without a prior evidence-backed interpretation or a current seasonal-drop consumer | No current exact id, string set, or product flow was found. |
| 2026-05-dm-header-activity | 2026-07-22T22:30:57Z | deleted | deleted without a prior interpretation or current DM-header activity consumer | No exact id or behavior-linked header component remains. |
| 2026-03-shop-fiat-prioritization | 2026-07-22T19:46:22Z | deleted | deleted without a prior interpretation or current Shop payment-priority consumer | No current exact id or checkout placement read was found. |
| 2026-05-gdop-v2-upsell | 2026-07-22T18:12:30Z | deleted | deleted with only an enabled flag and no prior interpretation or current upsell consumer | No exact id, visible GDOP surface, or behavior-linked read remains. |

## 중요한 실험 상세 해석

### 즐겨찾는 채널의 제한적 무료 접근

- id: `2026-01-favorites-server`
- 요약: 즐겨찾는 채널을 전용 Favorites 목록으로 묶고, 일부 비구독 사용자에게도 제한적으로 열어 주는 실험입니다.
- 근거: 현재 접근 도우미가 isFreemium을 직접 읽고 비구독 비교안의 한도를 3개로 계산합니다.
- source_context: Favorites access helper, isFreemium, favoriteLimit

### Living Room 비교안 세분화

- id: `2026-06_guild_rooms`
- 요약: 서버 음성 채널을 좌석과 방이 있는 Living Room 형태로 바꾸는 기존 실험을 더 세분화했습니다.
- 근거: enabled는 방·좌석 흐름에서, interactionsEnabled는 방 안 위치에 맞춘 음성 처리에서 계속 소비됩니다.
- source_context: RTCConnection, VOICE_STATE_UPDATES, GuildRoomSpatialAudioManager

### 서버 관리용 Guild Space

- id: `2026-06_guild_spaces`
- 요약: 서버 관리 권한이 있는 사용자에게 Guild Space 또는 Server Hub 화면을 여는 서버 실험입니다.
- 근거: Guild Space 경로는 서버 실험과 Manage Guild 권한을 모두 통과할 때만 접근 가능합니다.
- source_context: GUILD_SPACE route, ChannelRenderer, Server Hub

### Nitro 연체 결제 바로가기

- id: `2026-07-past-due-checkout`
- 요약: Nitro 결제가 연체됐을 때 관련 버튼을 미납 청구서 결제 흐름으로 연결하는 실험입니다.
- 근거: 연체 상태와 열린 청구서를 확인한 뒤 관련 안내 버튼을 해당 청구서 결제 화면으로 연결합니다.
- source_context: PAST_DUE, open invoice, checkout

### 새 연령 확인 시작 화면

- id: `2026-07-expressive-modal-v2`
- 요약: 연령 확인을 시작할 때 기존 안내 대신 새 표현형 모달을 보여 주는 실험입니다.
- 근거: 일반 연령 확인 시작 경로가 진입 위치별 설정값을 읽어 별도의 새 모달을 선택합니다.
- source_context: age verification entry point, methods v2, expressive modal

### 서버 안의 Magic Builder

- id: `2026-07-vibegrations-guild`
- 요약: 서버 관리자가 채팅에서 앱을 만들고 미리보기한 뒤 Discord에 배포하는 Magic Builder 흐름을 여는 실험입니다.
- 근거: 서버·채널 관리 권한과 실험을 함께 확인하며, 문자열은 생성부터 미리보기·게시·삭제까지의 전체 흐름을 제공합니다.
- source_context: Magic Builder, preview server, Publish to Discord

### NVIDIA 영상 인코딩 옵션

- id: `2026-07-nvenc-reconstructed-frames`
- 요약: NVIDIA 그래픽카드로 화면 공유 영상을 압축할 때 재구성 프레임 방식을 적용하는 실험입니다.
- 근거: 영상 인코더 옵션 생성 경로가 설정값을 읽어 nvReconFrames를 추가합니다. 화질·성능 방향은 아직 확인되지 않았습니다.
- source_context: getVideoEncoderExperiments, nvReconFrames, MediaEngine

### 프로필 표시 범위 재확인

- id: `2026-04-consistent-profiles`
- 요약: 멤버 목록과 활동 헤더에서 길드 태그와 아바타 장식을 같은 새 프로필 방식으로 표시하는 실험입니다.
- 근거: 멤버 목록과 Now Playing 헤더가 같은 enabled 도우미를 읽으며, 확인되지 않았던 두 번째 비교안은 이번 행에서 제거됐습니다.
- source_context: PeopleUserInfo, NowPlayingHeader, avatar decoration

## 실험에서 나타나지 않는 변화

| area | summary | evidence_notes | confidence |
| --- | --- | --- | --- |
| Magic Builder 앱 제작·배포 | 아이디어 작성, 자동 빌드, 앱 미리보기, 테스트 서버, 봇 권한, Discord 게시, 프로덕션 게시와 앱 삭제까지 이어지는 서버용 앱 제작 흐름이 대규모로 추가됐습니다. | Current-window strings cover planning, dependency installation, health checks, preview deployment, permissions, publishing, production, and permanent deletion. | high |
| 게임 서버 생성·요금제·해지 관리 | Shop에서 게임 서버를 만들고 플랜을 고르며, 업그레이드·다운그레이드·재활성화·해지일과 데이터 삭제 결과를 확인하는 흐름이 영어와 한국어로 확장됐습니다. | Strings cover plan selection, prorating, renewal, instance limits, cancellation dates, keeping a server, and permanent server-data deletion. | high |
| 저장한 메시지와 리마인더 분리 | 메시지를 저장하는 설명에서 리마인더를 분리하고, 리마인더 전용 빈 화면과 제거 동작을 추가했습니다. | Existing bookmark copy drops reminder wording while new strings add reminder-specific empty states and Remove Reminder. | high |
| 연령 확인 방식 v2 | 연령 확인 방식을 불러오는 v2 API와 방식 로딩·실행 오류 문구가 추가돼, 확인 수단 선택 흐름이 별도로 정비되고 있습니다. | Both API aliases add /age-verification/methods/v2, accompanied by method-loading and method-opening errors. | high |
| 파트너 스토어 출시 신호 | 파트너 SDK의 스토어 적격성 조회 경로가 삭제되고 출시 알림 경로가 추가돼, 적격성 확인에서 스토어 공개 시점 알림으로 무게가 이동했습니다. | The storefront-eligibility aliases are deleted while storefront-launch-announcement aliases are added at the same timestamp. | medium |
| 주문 취소 서명 단계 | 결제 주문을 취소할 때 서명 또는 확인 단계를 위한 새 API 경로가 추가됐습니다. | ORDER_CANCEL_SIGNING and its ENDPOINT alias both map to /billing/orders/:param/cancel-signing. | high |
| Nitro 프로필 프리셋 미리보기 | Nitro 꾸미기를 무작위 프로필 룩으로 시험하고, 프리셋 이름과 현재 미리보기 상태를 안내하는 문구가 추가됐습니다. | Four strings cover a random Nitro look, named profile presets, the active preview, and returning to the styles overview. | high |
| 음성 연결 상태 용어 변경 | 음성 연결 대기 상태가 기술적인 ‘Awaiting Endpoint’에서 ‘Waiting for Voice Server’로 바뀌어 사용자에게 원인을 더 직접 설명합니다. | English and Korean Awaiting Endpoint rows are removed while Waiting for Voice Server is added. | high |
| Collectibles Collabs·할인·Orbs 정리 | Shop에 Collabs와 개수 표시, Offer Eligible 문구가 추가된 반면 기존 할인 안내와 Nitro 월간 Orbs 업셀 문구는 삭제됐습니다. | Collabs filter labels and counts arrive after English/Korean discount and monthly-Orbs copy is removed. | high |
| Guild Rooms 방 선택 | 서버 음성 공간에서 사용할 방을 고르는 ‘Choose a Room’, 방 선택 안내, ‘Living Room’ 문구가 추가됐습니다. | Three strings form a complete room-selection prompt and match the current Guild Rooms consumers. | high |
| 메시지 유형·반응 알림 | 이미지, 영상, GIF, 파일, 설문, 음성 메시지와 전달 메시지를 구분하는 알림과 반응 도달 문구가 확장됐습니다. | English reaction strings and Korean message-summary strings enumerate media and attachment types. | high |
| 프로필·게임·Clips 접근성 문구 | 게임 선호도, 프로필 사진 보기, Shop this Look, Clips 자르기 위치와 초기화 상태, 이미지 편집기의 키보드 위치 안내가 한국어 데이터에 추가됐습니다. | The Korean cluster covers favorite games, profile preview, decoration discovery, crop positions, clip initialization, and arrow-key placement. | high |
| 기타 문구 정리와 일시적 churn | GIF 팁에서 /tenor가 빠지고, 게시물·스레드 보관 문구는 같은 창에서 삭제와 재추가가 반복됐으며, 모바일 위젯 편집 제한과 글자 수 접근성 안내가 추가됐습니다. | These rows are concrete copy changes, but the archive add/delete cycle does not support a product rollout conclusion. | high |

## Unresolved 후보와 다음 확인 포인트

- 현재 unresolved 후보는 34개입니다. 이전 33개를 먼저 재검색했고, 삭제된 `2026-06-bounty-use-video-modal-mobile-placement-experiment`는 보존할 해석이 없어 후보에서 제거했습니다.
- 이번 창에서는 Quest Home 타일 재설계와 Collectibles Collabs 필터를 새 후보로 추가했습니다. 두 항목 모두 제품 표면이나 설정 정의는 있지만 이를 실제로 읽는 화면 소비가 확인되지 않아 public analysis를 비워 두었습니다.

| id | timestamp | status | reason | next_check_hint |
| --- | --- | --- | --- | --- |
| 2026-06-remove-wishlist-dm-sidebar-side-copy | 2026-06-10T15:05:19Z | needs_evidence | no current experiment id, config consumer, or wishlist DM-sidebar copy surface found | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-05-dvp-for-attachments | 2026-06-12T20:47:43Z | needs_evidence | no current experiment id or config consumer; attachment/viewer strings are still not enough to link the feature | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-05-bounties-stage-1 | 2026-06-13T03:48:57Z | needs_evidence | the definition remains unassigned near Quest/Bounties code; timer, Orbs amount, scrolling, and looping keys still have no confirmed config consumer | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-server-setup-boost-cta | 2026-06-15T22:06:33Z | needs_evidence | server perk and Boost copy exists, but no current experiment id or config consumer links server setup to a Boost CTA | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-non-friend-messages-requests-in-uk | 2026-06-18T18:30:11Z | needs_evidence | no current experiment id or consumer ties UK users to a changed non-friend message-request path | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-clips-editor-v2 | 2026-06-22T21:21:29Z | needs_evidence | the current bundle still has no exact id or config consumer; new Clip Quality copy confirms a settings surface but does not link it to this experiment | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-mobile-server-tag | 2026-06-23T05:14:29Z | needs_evidence | the registration remains unassigned; the new guild-profile-server-tag row and server-tag copy do not establish this experiment's visible mobile consumer | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-polls-click-to-profile | 2026-06-26T19:09:12Z | needs_evidence | no current experiment id match or poll-click profile consumer found | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-game-invites-channel | 2026-06-26T21:06:12Z | needs_evidence | new built-in-voice LFG copy confirms a product surface, but no current exact id or config consumer links it to this experiment | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-similar-games-desktop | 2026-06-26T22:39:05Z | needs_evidence | new game-profile preference and autocomplete copy appeared, but no exact id or similar-games desktop consumer was found | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-similar-games-mobile | 2026-06-26T22:39:05Z | needs_evidence | new game-profile preference and autocomplete copy appeared, but no exact id or similar-games mobile consumer was found | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-orb-redemptions-billing-history | 2026-06-30T01:03:49Z | needs_evidence | partner and Orbs benefit copy changed, but no exact id or billing-history config consumer links those strings to this experiment | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-05-clips-timeline | 2026-06-30T18:26:23.440905+00:00 | needs_evidence | no current experiment id or Clips timeline consumer found in the current bundle | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-server-boost-bar-nudge | 2026-06-30T19:02:56Z | needs_evidence | server perk and Boost copy exists, but no current experiment id or config consumer links the Boost bar nudge to a visible surface | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-improved-shop-loading | 2026-06-30T20:47:50Z | needs_evidence | no current experiment id or Shop loading consumer found | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-game-profile-share-link | 2026-07-01T02:02:49.926027+00:00 | needs_ui_consumer | the current consumer still confirms coded-link analytics only; showSmallEmbed has no user-visible consumer | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-07-server-tag-game-profiles-desktop | 2026-07-06T17:01:20Z | needs_evidence | a new guild-profile-server-tag row and game-profile copy appeared, but no exact id or desktop server-tag consumer was confirmed | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-quest-home-layout-visual-tweaks | 2026-07-07T23:29:41.973954+00:00 | needs_config_consumer | the definition and exported helper remain, but no current visible layout read was confirmed | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-07-activity-entrypoint-ui | 2026-07-09T15:00:53Z | needs_evidence | new activity accessibility strings confirm an activity surface, but no exact id or activity-entrypoint config consumer was found | Look for an exact id match or a consumer tied to the activity panel entrypoint before writing public analysis. |
| 2026-07-smag-wishlist-recommendations-dismiss-threshold | 2026-07-09T22:37:43Z | needs_evidence | wishlist routes and a new direct-to-gifting row are present, but no exact id or dismissal-threshold consumer was found | Recheck wishlist recommendation modules for a dismissal counter or threshold config consumer. |
| 2026-07-smag-wishlist-nitro-first-slot | 2026-07-10T00:43:48Z | needs_evidence | wishlist routes and a new direct-to-gifting row are present, but no exact id or Nitro-first-slot consumer was found | Search current wishlist recommendation rendering for a Nitro-first-slot config read or visible placement consumer. |
| 2026-07-smag-dm-sidebar-nitro-recommendation | 2026-07-10T16:35:32Z | needs_evidence | wishlist routes and a new direct-to-gifting row are present, but no exact id or DM-sidebar Nitro recommendation consumer was found | Look for a DM sidebar recommendation component that reads this experiment or a matching config export. |
| 2026-07-shop-this-look | 2026-07-10T17:43:08Z | needs_evidence | Korean Shop this Look and friend-decoration copy confirm the discovery surface, but the exact experiment id and config consumer remain absent | Re-search Shop/Collectibles chunks for a consumer that ties the string to the experiment before adding analysis. |
| 2026-07-quest-bar-secondary-cta | 2026-07-10T22:13:34Z | needs_evidence | the definition remains with showPlayInstantlyLabel, but no exported-symbol or component consumer was found | Find a Quest bar component that reads the exported experiment before writing user-facing analysis. |
| 2026-07-bounties-vertical-scroll | 2026-07-15T17:51:39Z | needs_config_consumer | vertical-scroll, affordance, auto-scroll, and peek settings are registered, but the registration result is not assigned or read | Find a Quest or Bounties component that reads the experiment result before writing public analysis. |
| 2026-07-collectibles-promotion-endpoint-reference | 2026-07-15T23:56:50Z | needs_experiment_linkage | Collabs and Offer Eligible counts add Shop filter evidence, but no exact experiment or endpoint consumer links the promotion row to a visible offer | Recheck Collectibles promotion-fetch code for this exact id or a returned offer object tied to a visible Shop surface. |
| 2026-06-wysiwyg-user-profile-premium-try-it-out | 2026-07-17T05:29:05Z | needs_experiment_linkage | new profile-preset and random Nitro-look strings further confirm the visible preview flow, but no exact experiment id or config consumer links that flow to this row | Find the WYSIWYG profile preview component and confirm that it reads this experiment before writing public analysis. |
| 2026-03-boost-to-unlock-mobile-coachmark | 2026-07-17T18:39:48.052938+00:00 | needs_ui_consumer | GuildPowerupsManager still reads showCoachmark only for powerup data fetching; no visible coachmark consumer was found | Trace the mobile Boost coachmark component and confirm that the fetched powerup state plus this experiment controls its visibility. |
| 2026-07-wishlist-direct-to-gifting | 2026-07-21T16:05:07Z | needs_experiment_linkage | wishlist and gifting flows exist, but no exact experiment match or variant consumer links them to this row | Find a wishlist item or gifting action that reads this experiment and distinguishes Variant 1 from Variant 2 before writing public analysis. |
| 2026-06-guild-profile-server-tag | 2026-07-21T17:09:42Z | needs_experiment_linkage | server-tag state and profile copy exist, but no exact experiment match or config consumer connects this row to the visible guild profile | Trace guild-profile tag rendering to an exact experiment read or matching exported helper before writing public analysis. |
| 2026-06-game-server-hosting-in-shop | 2026-07-21T18:01:14Z | needs_experiment_linkage | game-server creation, plans, limits, management, and cancellation copy now confirms a broad Shop surface, but no exact experiment or treatment consumer maps its variants | Find a Shop game-server card or route that reads this experiment and maps its three variants to visible placement behavior. |
| 2026-07-powerups-coachmark-scroll-close | 2026-07-21T23:35:16Z | needs_ui_consumer | Powerups coachmark code exists, but no exact experiment match or scroll-close consumer links that behavior to this row | Trace the visible Powerups coachmark close handler and confirm that scrolling reads this experiment before writing public analysis. |
| 2026-07-collectibles-collabs-filter | 2026-07-22T18:21:37Z | needs_experiment_linkage | Collabs, Collabs counts, and Offer Eligible counts confirm a Shop filter surface, but no exact experiment id or filter consumer was found | Trace the Shop filter rendering and confirm an exact experiment read before adding public analysis. |
| 2026-05-quest-home-tile-redesign | 2026-07-22T23:47:28.283974+00:00 | needs_config_consumer | the current definition is exported and adds a clickable-tile treatment, but no import site reads the exported experiment object | Find a Quest Home tile or layout component that reads the exported experiment object before writing public analysis. |

## 검증 및 커밋/푸시 결과

- JSON 유효성: passed
- 리포트 구조: passed
- 금지 fallback 문구 검색: passed
- 공개 내용 점검: passed
- 최신 리포트 포인터 일치: passed
- git diff 검사: passed
- 커밋/푸시: passed (`f181432f84` pushed to `origin/main`; metadata recorded by follow-up commit)
- 비고: No application or parser code changed, so code build checks are not required for this run.

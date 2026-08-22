# Discord 데이터마이닝 주간 리포트 — 2026-08-22

## 처리 기간과 빌드

- 처리 기간: `2026-08-19T04:08:23Z` ~ `2026-08-22T04:02:32Z`
- build_hash: `2cd89e1a1aa5483dd4412bc87f2d90a859b025a2`
- 근거 번들: `canary/web.01df9df165da1dfb.js`
- 입력 기준: history.json을 우선 확인하고 current private extraction history 및 tracked data/web/*와 대조했습니다. public history에 빠진 문자열 3행을 동기화했으며, latest_changes.json은 마지막 빌드의 영어 문자열 3개만 담고 있어 보조 신호로만 사용했습니다.

## 핵심 요약

- 실험 4행 / 3개 ID, API 2행(1개 URL), 문자열 196행(191개 고유 행)을 검토했습니다.
- disposition은 strengthened_existing 3행, unresolved_needs_evidence 1행입니다.
- 공간 음향 실험 2행은 현재 출력 장치 메뉴·기기 지원·음성 엔진 소비 근거로 기존 해석을 현재 빌드에 맞게 보강했습니다.
- Nitro 맞춤 혜택 UI 실험 1행은 내부 축약 참조만 달라져 기존 사용자 해석을 현재 Nitro 탭 소비 근거로 보강했습니다.
- 수동 연령 확인 fallback은 정확한 helper가 실험을 읽지만 실제 호출부가 없어 public analysis를 넣지 않고 unresolved로 남겼습니다.
- 이전 unresolved 42개를 모두 재검색했으며 승격·제거 없이 유지해 총 43개가 됐습니다.
- 비실험 변화로 연령 확인 이어하기, 앱 제작 외부 도구/MCP, 설정·비밀값, 공유·버전 복원, 이미지 편집, 선물 Orbs 보상, 지원 진단과 지역 제한 안내를 묶어 정리했습니다.

## 실험 전수 분석 결과

### interpreted

| ID | 시각 | 상태 | 판단 | 근거 |
|---|---|---|---|---|
| — | — | — | 해당 없음 | 이번 처리 창에 해당 행이 없습니다. |

### strengthened

| ID | 시각 | 상태 | 판단 | 근거 |
|---|---|---|---|---|
| `2026-05-spatial-audio-for-voice` | `2026-08-19T19:01:08.382923+00:00` | modified | strengthened_existing | 현재 출력 장치 메뉴와 음성 엔진이 실험 설정 및 기기 지원 여부를 함께 읽는 흐름을 다시 확인해 기존 해석을 현재 빌드 근거로 갱신했습니다. |
| `2026-05-spatial-audio-for-voice` | `2026-08-19T21:38:09.699230+00:00` | modified | strengthened_existing | 같은 날의 두 번째 raw 수정에서도 켜짐·꺼짐 비교안은 유지됐고 현재 메뉴·음성 처리 소비가 계속 확인됩니다. |
| `2026-06-ml-offer-creation-ui-upgrade` | `2026-08-21T15:17:57.523414+00:00` | modified | strengthened_existing | Nitro 탭 버튼이 배지 모양과 안내 표면을 계속 직접 읽으며, 이 행의 raw 변화는 내부 축약 참조만 바꿉니다. |

### unresolved

| ID | 시각 | 상태 | 판단 | 근거 |
|---|---|---|---|---|
| `2026-07-manual-age-assurance-fallback` | `2026-08-20T06:27:03Z` | added | unresolved_needs_evidence | 연령 확인 시스템 메시지의 수동 검토 표시를 판정하는 helper가 이 실험을 읽지만, 현재 번들에서 그 helper를 호출해 실제 버튼을 그리는 화면은 찾지 못했습니다. |

### skipped

| ID | 시각 | 상태 | 판단 | 근거 |
|---|---|---|---|---|
| — | — | — | 해당 없음 | 이번 처리 창에 해당 행이 없습니다. |

## 중요한 실험 상세 해석

### 음성 통화 공간 음향 (`2026-05-spatial-audio-for-voice`)

지원되는 기기에서 음성 출력 메뉴에 공간 음향 스위치를 보여 주고, 음성 통화 참가자 소리를 입체적으로 배치할 수 있게 합니다.

- 근거: 현재 출력 장치 메뉴가 실험과 기기 지원을 함께 확인해 스위치를 렌더링하고, 음성 엔진도 같은 조건으로 공간 처리를 적용합니다.
- 확인 단서: AudioDeviceMenu, Spatial Audio, SPATIAL_AUDIO capability, MediaEngineStore

### 수동 연령 확인 fallback (`2026-07-manual-age-assurance-fallback`)

연령 확인 시스템 메시지에서 수동 검토 선택지를 허용하려는 설정으로 보이지만, 실제 버튼을 그리는 호출 경로는 아직 확인되지 않았습니다.

- 근거: 정확한 실험과 request_manual_review를 함께 검사하는 helper는 있으나 현재 번들에 caller가 없습니다.
- 확인 단서: request_manual_review, age-verification system message, Confirm your age group

### Nitro 맞춤 혜택 표시 (`2026-06-ml-offer-creation-ui-upgrade`)

Nitro 탭의 맞춤 혜택 배지를 그라데이션·강조형·빛나는 모양으로 나누고 말풍선이나 도움말 노출을 비교합니다.

- 근거: 현재 Nitro 탭 버튼이 두 설정을 계속 직접 읽고 있으며, 이번 raw 수정은 사용자 비교안이 아닌 내부 축약 참조만 바꿉니다.
- 확인 단서: NitroTabButton, badgeStyle, surface

## 실험에서 나타나지 않는 변화

- API endpoint 변경은 2행이며 두 alias가 같은 일반 마케팅 캠페인 eligibility URL의 삭제를 나타냅니다. 이 기록만으로 서버 기능 제거 또는 선물 보상 흐름의 종료를 단정하지 않습니다.

| 영역 | 제품 변화 | 근거와 확신도 |
|---|---|---|
| 연령 확인 이어하기와 연령대 확인 | 다른 창에서 진행 중인 연령 확인을 안내하고, 성인으로 확인될 때 열리는 연령 제한 콘텐츠와 설정을 설명하는 흐름이 추가됐습니다. | 같은 처리 창의 문자열이 다른 창에서 계속하기, 다른 방법 선택, 연령대 확인, 성인 확인 뒤 접근 범위를 하나의 사용자 흐름으로 설명합니다. (high) |
| 앱 제작 외부 도구 연결과 MCP | 앱 제작 프로젝트를 외부 코딩 도구에서 이어서 작업할 수 있도록 24시간 링크를 만들고 새 링크로 교체하는 흐름이 추가됐으며, 뒤이어 해당 진입점 문구가 MCP 연결 중심으로 바뀌었습니다. | 외부 도구용 링크 생성·만료·새로고침·연결 도구 갱신 문구가 함께 추가됐고, Build with your tools가 Conjuring MCP로 수정됐습니다. (high) |
| 앱 설정과 비밀값 보관 | 앱 설정과 비밀값을 구분해 저장하고, 비밀값은 채팅이나 도우미에게 보이지 않는 잠긴 보관소로 보내며 설정 변경 뒤 재빌드하는 흐름이 추가됐습니다. | App Settings, Secrets, locked vault, 저장 성공·실패, 설정 변경 뒤 rebuild 문구가 한 흐름을 구성합니다. 이전 플랫폼별 credential 입력 문구는 같은 창에서 삭제됐습니다. (high) |
| 앱 프로젝트 공유와 버전 복원 | 서버 안에서 프로젝트를 공개·비공개로 전환하고 공유받은 프로젝트를 확인하며, 저장된 버전 기록에서 이전 상태를 복원하는 흐름이 추가됐습니다. | Make public/private, shared projects, Version History, Restore, 현재 작업 보존과 복원 성공·실패 문구가 함께 나타납니다. (high) |
| 앱 미리보기와 이미지 편집 | 앱을 휴대전화 크기 또는 전체 크기로 미리 보고 파일·사진을 올리며, 이미지 자체를 교체·재배치·편집하는 제작 흐름이 확장됐습니다. | Preview at phone/full size, Files, Photos, Uploading과 마지막 빌드의 Edit/Change/Reposition Image 문자열이 편집 단계를 연결합니다. (high) |
| 선물 구매 Orbs 보상 | 선물 구매를 완료하면 5,000 Orbs를 받는다는 보상 안내와 여러 선물의 수량을 고르는 문구가 추가됐습니다. | 영어·한국어 보상 문구가 구매 완료 조건과 보상량을 명시합니다. 일반 마케팅 캠페인 eligibility URL의 두 alias는 삭제됐지만, 이 사실만으로 실제 서버 기능 제거를 뜻하지는 않습니다. (high) |
| 앱 제작 도우미 진행과 질문 제어 | 도우미가 작업에 쓴 시간을 보여 주고 완료·실패·중단 상태를 구분하며, 질문을 건너뛰거나 닫고 별도 대화를 이어 갈 수 있게 하는 흐름이 추가됐습니다. | Thought for, Finished/Couldn’t finish/Stopped, Skip to the next question, Or chat about it 문구가 작업 상태와 사용자 개입을 설명합니다. (high) |
| 성능 추적 지원 파일 | Discord 성능 정보를 30초 동안 기록해 다운로드 폴더에 저장하고 지원 티켓에 첨부할 수 있는 진단 흐름이 한국어 문자열에 나타났습니다. | 캡처 시작, 수집 중, 다운로드 폴더 저장, 지원 티켓 첨부 설명이 하나의 진단 절차를 이룹니다. (high) |
| 지역별 영상 기능 제한 안내 | 브라질 정부 명령에 따라 일부 지역에서 동영상 또는 화면 공유를 사용할 수 없다는 안내 문구가 한국어에 추가됐습니다. | 동영상 비활성화와 화면 공유 비활성화 문구가 같은 법적 사유와 지역 조건을 명시합니다. (high) |

## unresolved 후보와 다음 확인 포인트

| ID | 보류 이유 | 다음 확인 |
|---|---|---|
| `2026-05-dvp-for-attachments` | no current experiment id or config consumer; attachment/viewer strings are still not enough to link the feature | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-05-bounties-stage-1` | the current bundle still registers timer, Orbs, looping, and scroll settings without assigning or reading the experiment result | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-06-server-setup-boost-cta` | server perk and Boost copy exists, but no current experiment id or config consumer links server setup to a Boost CTA | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-06-non-friend-messages-requests-in-uk` | no current experiment id or consumer ties UK users to a changed non-friend message-request path | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-06-clips-editor-v2` | Auto Clips copy is present in the current window, but the exact experiment id and an editor-v2 consumer remain absent from the current bundle. | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
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
| `2026-06-wysiwyg-user-profile-premium-try-it-out` | current Korean Custom Widget and Nitro copy makes the visible profile-upsell surface clearer, but no exact experiment id or config consumer links it to this row | 커스텀 위젯 미리보기 renderer가 이 실험을 직접 읽는지 확인한 뒤 public analysis를 작성하세요. |
| `2026-03-boost-to-unlock-mobile-coachmark` | the mobile Powerups manager still reads showCoachmark only as part of its data-fetch decision; no visible coachmark renderer consumes the result | Trace the mobile Powerups coachmark renderer and confirm that the fetched data plus this experiment controls visible exposure before writing public analysis. |
| `2026-07-wishlist-direct-to-gifting` | wishlist and gifting flows exist, but no exact experiment match or variant consumer links them to this row | Find a wishlist item or gifting action that reads this experiment and distinguishes Variant 1 from Variant 2 before writing public analysis. |
| `2026-06-guild-profile-server-tag` | server-tag state and profile copy exist, but no exact experiment match or config consumer connects this row to the visible guild profile | Trace guild-profile tag rendering to an exact experiment read or matching exported helper before writing public analysis. |
| `2026-07-powerups-coachmark-scroll-close` | Powerups coachmark code exists, but no exact experiment match or scroll-close consumer links that behavior to this row | Trace the visible Powerups coachmark close handler and confirm that scrolling reads this experiment before writing public analysis. |
| `2026-07-collectibles-collabs-filter` | Collabs, Collabs counts, and Offer Eligible counts confirm a Shop filter surface, but no exact experiment id or filter consumer was found | Trace the Shop filter rendering and confirm an exact experiment read before adding public analysis. |
| `2026-05-quest-home-tile-redesign` | the current definition exports layout and clickable-tile options, but no current Quest Home component reads the exported experiment object | Find a Quest Home tile or layout component that reads the exported experiment object before writing public analysis. |
| `2026-07-nitro-home-header-followup` | Nitro Home and free Shop-item strings changed, but no exact experiment id or header variant consumer was found | Trace the Nitro Home header component and confirm how Variant 0 and Variant 1 change the visible header. |
| `2026-06-hero-shelf-ad-tile` | the row suggests a visible advertising tile, but no exact experiment id, shelf component, route, or treatment consumer was found | Find a rendered shelf or advertising card that reads this experiment before writing public analysis. |
| `2026-07-gdop-discovery` | no exact experiment id, config consumer, route, or visible discovery component was found | Find an exact experiment registration or discovery component that distinguishes Variant 0 from Variant 1. |
| `2026-07-social-layer-storefront-spend-orbs-banner-copy` | time-limited Nitro and Orbs item copy confirms a storefront banner surface, but no exact experiment id or variant consumer links that copy to this row | Trace the social-layer storefront banner renderer to an exact experiment read and compare the two copy variants. |
| `2026-07-call-of-duty-3pp-expired` | 새 Call of Duty nagbar는 nagbar 실험과 non-sub marketing gate를 직접 읽지만, expired helper는 현재 배너·보상 카드에서 호출되지 않습니다. | 만료 상태 화면이 expired helper를 직접 읽는 호출 경로를 찾은 뒤 public analysis를 작성하세요. |
| `2026-07-cod-3pp` | 새 Call of Duty nagbar와 Nitro 탭은 nagbar 및 marketing helper를 사용하지만, base experiment helper를 호출하는 현재 소비 위치는 없습니다. | Call of Duty 보상 진입점이 base helper를 직접 읽는 경로를 찾은 뒤 public analysis를 작성하세요. |
| `2026-07-wishlist-show-owned-items-last` | wishlist and gifting surfaces exist, but no exact experiment id or owned-item sorting consumer was found | Find the wishlist item sorter and confirm that it reads this experiment before moving owned items to the end. |
| `2026-08-soundboard-desktop-nux` | the desktop Soundboard introduction exists in localized copy, but no exact experiment id or config read links NUX exposure to this row | Trace the Soundboard NUX renderer to an exact experiment read before adding public analysis. |
| `2026-07-game-mentions-v2-mobile` | the exact mobile experiment remains registration-only; its returned config is not assigned or read by the mobile autocomplete path | Find the mobile game-mention autocomplete component that reads this experiment before writing public analysis. |
| `2026-07-clips-editor-text-track` | Clips now has title and text-or-image editing copy, but no exact experiment id, config object, or text-track consumer links those controls to this row | Find a Clips editor text or caption track component tied to this experiment before writing public analysis. |
| `2026-07-plan-select-ui-redesign` | yearly-switch copy was deleted in the same window, but no current exact experiment id or plan-selection variant consumer was found | Find a plan-selection screen that reads this experiment and compare Variant 0 with Variant 1 before writing public analysis. |
| `2026-08-hide-gift-shop-upsell` | gift and Shop purchase surfaces remain present, but no current exact experiment id or consumer that hides the upsell was found | Trace the gifting checkout or Shop upsell renderer to an exact experiment read before describing what is hidden. |
| `2026-07-custom-app-store-overlay` | the exact experiment remains registration-only beside the existing app-store overlay gate; no visible overlay component reads it | Find an overlay component that reads this exact experiment before describing how the custom app-store overlay differs from the existing feature gate. |
| `2026-08-premium-gifting-gogo-promotion` | the exact experiment is still read by the free-SKU-step helper, but no current module calls that export; new 5,000-Orb gift copy and deletion of a generic marketing eligibility alias do not establish the missing checkout caller | 선물 결제 화면이 free-SKU helper 또는 새 eligibility hook을 호출하고 enabled 상태에서 단계가 어떻게 달라지는지 확인하세요. |
| `2026-08-profile-embed-share-button` | current Korean Share Profile copy confirms the product surface, but the exact experiment id and a config consumer are absent from the current bundle | Share Profile 버튼 renderer가 정확한 실험을 읽는 경로를 찾은 뒤 노출 조건이나 배치를 설명하세요. |
| `2026-07-manual-age-assurance-fallback` | the exact experiment gates a helper that recognizes request_manual_review in age-verification system messages, but no current module calls the exported helper, so a visible manual-review fallback is not confirmed | Trace the age-verification system-message CTA renderer to the exported helper and confirm what action starts after a user requests manual review. |

## 검증 및 커밋/푸시 결과

- JSON/report shape, exact private/public/web parity, 한영 해석 203행, unresolved 43건, raw 필드·latest_changes 불변성, 금지 문구, report pointer, 공개 저장소 12개 테스트, 비공개 보안·파서 테스트, scoped 공개 경로 보안 검사, git diff 검사가 통과했습니다.
- 데이터·리포트 커밋 `844e5aec76dc`와 최종 메타데이터 follow-up 커밋을 `origin/main`에 push했습니다.

### Security/privacy impact

신뢰 경계, 수집, 전송, 보존, 삭제, 백업, 접근권한, 공개 schema는 바뀌지 않았습니다. 공개 Discord 제품 메타데이터 해석과 집계 근거만 추가했으며 사용자 식별자, 메시지 본문, 자격증명, private runner state, private parser logic은 포함하지 않았습니다.

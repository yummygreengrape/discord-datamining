# Discord Datamining Weekly Interpretation Report - 2026-07-04

## 처리 기간 / Build
- 처리 기간: 2026-07-02T11:04:29Z ~ 2026-07-04T04:01:18Z (이전 성공 cutoff 이후, KST 실행일 2026-07-04)
- build_hash: 15dff22fc22c133336320b62b723571500efe05a
- source bundle: canary/web.7dc0925a92aa0805.js
- 실험 row 6개 / 고유 id 5개, API row 2개, 문자열 row 178개를 확인했습니다.
- disposition: interpreted 4, strengthened_existing 2

## 핵심 요약
- `latest_changes.json`의 실험/API 배열은 비어 있었지만, `history.json` 기준으로 cutoff 이후 실험 6행과 API/문자열 변경이 확인됐습니다.
- 새 public analysis는 Quest Home 진입점 강조, Nitro 선물 수량 선택, 사운드보드 자주 사용 섹션에 추가했습니다.
- 기존 해석은 사운드보드 높이와 Nitro 탭 맞춤 혜택 실험에서 현재 Canary 사용처를 다시 확인해 새 row와 기존 row에 동기화했습니다.
- unresolved 후보는 먼저 재검색했고, 새 사용자-facing 소비 근거가 부족한 항목은 full metadata를 보존해 carry-forward했습니다.

## 실험 전수 분석 결과
### Interpreted / Newly Added
|id|status|importance|summary|
|---|---|---|---|
|2026-07-odyssey-hero-temp-overrides|added|medium|Quest Home 진입 버튼에 캠페인용 강조 배경을 임시로 적용하는 실험입니다.|
|2026-06-bulk-nitro-gifting|added/modified|medium|Nitro 선물 결제에서 같은 선물을 여러 개 고르는 수량 선택 UI를 시험합니다.|
|2026-06-soundboard-frequently-used|added|medium|사운드보드에 자주 쓴 소리 섹션을 추가하는 실험입니다.|

### Strengthened / Filled Existing
|id|status|importance|summary|
|---|---|---|---|
|2026-06-soundboard-picker-height|modified|low|사운드보드 선택기 팝아웃을 100px 더 높게 보여주는 실험입니다.|
|2026-06-ml-offer-creation-ui-upgrade|modified|medium|Nitro 탭의 맞춤 혜택 배지 모양과 안내 방식을 바꾸는 실험입니다.|

### Unresolved
|id|status|reason|
|---|---|---|
|2026-05-dvp-for-attachments|needs_evidence|no current experiment id or config consumer; attachment/viewer strings are still not enough to link the feature|
|2026-06-remove-wishlist-dm-sidebar-side-copy|needs_evidence|no current experiment id, config consumer, or wishlist DM-sidebar copy surface found|
|2026-06-bounty-use-video-modal-mobile-placement-experiment|needs_evidence|experiment definition still exists near Quest/Bounties code, but no assigned config read for mobile video modal placement was found|
|2026-05-bounties-stage-1|needs_evidence|definition still exists near Quest/Bounties code and a bounty Orbs string appeared, but timer, Orbs amount, scrolling, and looping keys still have no confirmed experiment config consumer|
|2026-06-quest-home-layout-visual-tweaks|needs_evidence|definition/export still exists in the Quest experiment module, but no current helper consumer was confirmed|
|2026-06-server-setup-boost-cta|needs_evidence|boost/server theme strings appeared, but no current experiment id or config consumer links server setup to a Boost CTA|
|2026-06-non-friend-messages-requests-in-uk|needs_evidence|no current experiment id or consumer ties UK users to a changed non-friend message-request path|
|2026-06-clips-editor-v2|needs_evidence|no current experiment id or config consumer ties Clips editor strings or UI to this experiment|
|2026-06-mobile-server-tag|needs_evidence|current guild settings/store module registers the experiment, and server tag strings appeared, but the experiment result is not assigned or read|
|2026-05-quest-tile-cta-refactor|needs_evidence|definition/export still exists in the Quest experiment module, but no current helper consumer was confirmed|
|2026-06-polls-click-to-profile|needs_evidence|no current experiment id match or poll-click profile consumer found|
|2026-06-game-invites-channel|needs_evidence|game and voice/social play strings changed, but no current experiment id or config consumer links them to the guild experiment|
|2026-06-similar-games-desktop|needs_evidence|no current experiment id match or similar-games desktop UI/API consumer found|
|2026-06-similar-games-mobile|needs_evidence|no current experiment id match or similar-games mobile UI/API consumer found|
|2026-06-wishlist-pdp-gift-button-priority|needs_evidence|no current experiment id or gift button priority consumer found|
|2026-06-server-boost-bar-nudge|needs_evidence|boost theme strings appeared, but no current experiment id or config consumer links the server Boost bar nudge to a visible surface|
|2026-06-improved-shop-loading|needs_evidence|no current experiment id or Shop loading consumer found|
|2026-05-clips-timeline|needs_evidence|no current experiment id or Clips timeline consumer found in the current bundle|
|2026-06-orb-redemptions-billing-history|needs_evidence|Orbs/Nitro redemption strings changed in-window, but no current experiment id or config consumer ties billing history behavior to this experiment|
|2026-06-game-profile-share-link|needs_ui_consumer|current consumer confirms game-profile coded-link analytics tracking, but showSmallEmbed or another user-visible UI consumer was not found|

### Skipped / No Public Analysis
이번 처리 창의 새 실험 row 중 public analysis 없이 skipped 처리한 항목은 없습니다. 다만 carry-forward unresolved 후보는 위 표처럼 계속 보류했습니다.

## 중요한 실험 상세 해석
### 2026-07-odyssey-hero-temp-overrides
- 요약: Quest Home 진입 버튼에 캠페인용 강조 배경을 임시로 적용하는 실험입니다.
- 상세: 친구/DM 목록의 Quest Home 항목을 그릴 때, 서버에서 Quest Home 진입점의 강조 배경 정보가 내려오면 비교안은 기본 색상 대신 노란색·빨간색·주황색 계열의 빛 효과를 씁니다. 버튼이 이동하는 대상은 Quest Home 그대로이며, 현재 확인된 변화는 진입 버튼을 더 눈에 띄게 보이게 하는 시각 처리입니다. 같은 코드 흐름에서 tooltip이나 이미지가 함께 내려오면 Quest Home 항목 안에 보조 배지나 이미지를 같이 보여줄 수 있습니다.
- 왜 중요한가: Quest나 보상 캠페인을 찾는 사용자가 왼쪽 목록에서 Quest Home을 더 빨리 알아보게 만드는 변화입니다. 기능 자체를 새로 여는 실험이라기보다는 특정 캠페인 진입점을 강조하는 실험으로 보는 것이 근거에 맞습니다.
- 근거: canary/web.7dc0925a92aa0805.js module 2716 reads the experiment with useConfig at the private channels list location.; When enabled and questHomeEntrypoint.gradientPreset is present, the Quest Home list item uses a custom yellow/red/orange hover gradient instead of the preset gradient.; The same UI path renders Quest Home text, optional tooltip badge, and optional entrypoint image.

### 2026-06-bulk-nitro-gifting
- 요약: Nitro 선물 결제에서 같은 선물을 여러 개 고르는 수량 선택 UI를 시험합니다.
- 상세: Nitro 선물 흐름에서 Tier 2 Nitro 플랜을 선택한 상태이고 비교안이 켜져 있으면, 플랜 선택 행 아래에 수량 조절 컨트롤이 나타납니다. 현재 확인된 UI는 1개부터 50개까지의 수량을 고를 수 있게 되어 있으며, 결제 상태도 선택한 수량을 저장하고 구매 요청에 수량을 전달할 수 있습니다. 같은 시점의 문자열에는 “{quantity} × {label}” 형식의 수량 표시 문구가 추가되어, 결제 화면에서 여러 개의 같은 항목을 묶어 보여주는 흐름을 뒷받침합니다.
- 왜 중요한가: 한 번에 여러 Nitro 선물을 준비하는 사용자는 반복 결제 없이 수량을 조절할 수 있습니다. 다만 현재 근거는 선물 결제 UI와 구매 요청의 수량 처리이며, 수령자 배분 방식까지는 이 변경만으로 확정할 수 없습니다.
- 근거: canary/web.7dc0925a92aa0805.js module 135314 reads the experiment with useConfig at PremiumSwitchPlanSelectOption.; The selected gift plan row renders a quantity stepper when the experiment is enabled for Tier 2 Nitro gifts.; Checkout state stores quantity, the SKU purchase request can include quantity, and string history adds “{quantity} × {label}”.

### 2026-06-soundboard-frequently-used
- 요약: 사운드보드에 자주 쓴 소리 섹션을 추가하는 실험입니다.
- 상세: 사운드보드가 사용 가능한 소리와 즐겨찾기 목록을 만든 뒤, 비교안이 켜져 있고 최근 자주 쓴 소리가 있으면 별도의 “자주 사용” 섹션을 끼워 넣습니다. 이미 즐겨찾기에 들어간 소리는 이 섹션에서 제외하고, 최대 3개의 최근 사용 소리를 우선 보여주는 흐름이 확인됩니다. 같은 코드 흐름에서는 이 섹션이 생길 때 팝아웃 높이를 100px 늘려 목록이 지나치게 답답해지지 않도록 합니다.
- 왜 중요한가: 사운드보드를 반복해서 쓰는 사용자는 최근에 많이 누른 소리를 더 빨리 찾을 수 있습니다. 즐겨찾기와는 다른 자동 추천 성격의 섹션이므로, 실제 사용 패턴이 사운드보드 탐색 순서에 영향을 주는 변화입니다.
- 근거: canary/web.7dc0925a92aa0805.js module 333216 reads the experiment with useConfig in the sound grid path.; The consumer filters frequently used sound IDs, excludes favorites, and inserts a FREQUENTLY_USED section when enabled.; The same module can add 100 px of popout height when the frequently-used section path is enabled.

### 2026-06-soundboard-picker-height
- 요약: 사운드보드 선택기 팝아웃을 100px 더 높게 보여주는 실험입니다.
- 상세: 사운드보드가 이모지 선택기 안이 아니라 독립 팝아웃으로 열릴 때, 비교안은 기본 높이 420px에 100px를 더한 크기를 적용합니다. 현재 config는 별도 픽셀 값을 내려보내기보다 켜짐 여부로 이 추가 높이를 결정합니다. 같은 코드 흐름에서는 자주 쓴 소리 섹션이 켜진 경우에도 같은 추가 높이를 적용할 수 있어, 사운드 목록이 길어질 때 한 화면에 더 많은 항목을 보여주려는 변화로 해석됩니다.
- 왜 중요한가: 서버 사운드가 많거나 자주 쓰는 소리 섹션이 생긴 경우 스크롤 부담을 줄일 수 있습니다. 작은 UI 크기 변경이지만 사운드보드를 자주 여는 사용자에게는 탐색 속도에 영향을 줄 수 있습니다.
- 근거: canary/web.7dc0925a92aa0805.js module 333216 reads the experiment with useConfig in the soundboard popout path.; When enabled and the soundboard is not embedded in the expression picker, the popout style becomes height: 420 + 100.; The current raw config key is enabled; no extraHeightPx config key is present in this build.

### 2026-06-ml-offer-creation-ui-upgrade
- 요약: Nitro 탭의 맞춤 혜택 배지 모양과 안내 방식을 바꾸는 실험입니다.
- 상세: Nitro 탭 버튼에 맞춤 혜택이 있을 때, 비교안은 혜택 배지를 그라데이션·강조형·빛나는 모양 중 하나로 표시합니다. 혜택 설명은 아무것도 띄우지 않거나, 말풍선 또는 짧은 도움말로 보여 줄 수 있습니다. 현재 Canary에서도 Nitro 탭 버튼 렌더링 흐름이 이 설정을 직접 읽고 있어, 이전 해석의 사용자-facing 근거가 유지됩니다.
- 왜 중요한가: 사용자가 자신에게 제공된 Nitro 혜택을 더 쉽게 발견할 수 있는지와, 어느 정도의 강조가 과하지 않은지를 함께 비교할 수 있습니다.
- 근거: canary/web.7dc0925a92aa0805.js module 2716 reads the experiment with useConfig at NitroTabButton.; badgeStyle selects gradient, expressive, or glowing offer badges.; surface controls whether the offer uses no surface, a popover, or a tooltip.

## 실험에서 나타나지 않는 변화
- premium-billing-past-due-restore: Premium billing adds a past-due restore path for retrying payment or adding a new payment method. 근거: API rows add /billing/premium/past-due and strings add “Restore Subscription” plus “Your subscription is past due. Retry payment or add a new payment method to restore it.”
- family-center-guardian-access-spending-downtime: Family Center copy now more explicitly covers guardian connection deadlines, QR/link sharing, spending caps, purchase/gift summaries, and scheduled downtime. 근거: Korean string changes add guardian connection calls to action, spending limit warnings, purchase and gift summaries, and downtime copy.
- quests-orbs-nitro-redemption: Quest and Orbs copy points to special quests, Orbs earned from quests, and Nitro-only Orbs redemption paths. 근거: String rows include “Special Quests”, “Discord 퀘스트를 완료하여 Orbs 획득하기”, Nitro-only Orbs redemption, and “Finish all bounties for +{orbAmount, number} Orbs to unlock”.
- server-tags-and-boost-themes: Server tags and Boost-unlocked custom server themes continue to surface in user-facing copy. 근거: Strings describe custom server tags visible beside member names, server profile/application exposure, and Boost-unlocked custom themes.
- voice-channel-chat-toggle: Voice channel text chat gets explicit toggle copy. 근거: Strings add “음성 채널 채팅 토글” and a description for toggling the text chat panel of the currently connected voice channel.
- game-and-activity-status-copy: Game/activity presence copy adds active-time labels and match/game event labels. 근거: Strings include Active weekdays/weekends/every day, Buzzing morning/evening labels, Established date, and game/match event labels.

## Unresolved 후보와 다음 확인 포인트
- 2026-05-dvp-for-attachments: no current experiment id or config consumer; attachment/viewer strings are still not enough to link the feature 다음 확인: Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, or user-facing string linkage before writing public analysis.
- 2026-06-remove-wishlist-dm-sidebar-side-copy: no current experiment id, config consumer, or wishlist DM-sidebar copy surface found 다음 확인: Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, or user-facing string linkage before writing public analysis.
- 2026-06-bounty-use-video-modal-mobile-placement-experiment: experiment definition still exists near Quest/Bounties code, but no assigned config read for mobile video modal placement was found 다음 확인: Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, or user-facing string linkage before writing public analysis.
- 2026-05-bounties-stage-1: definition still exists near Quest/Bounties code and a bounty Orbs string appeared, but timer, Orbs amount, scrolling, and looping keys still have no confirmed experiment config consumer 다음 확인: Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, or user-facing string linkage before writing public analysis.
- 2026-06-quest-home-layout-visual-tweaks: definition/export still exists in the Quest experiment module, but no current helper consumer was confirmed 다음 확인: Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, or user-facing string linkage before writing public analysis.
- 2026-06-server-setup-boost-cta: boost/server theme strings appeared, but no current experiment id or config consumer links server setup to a Boost CTA 다음 확인: Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, or user-facing string linkage before writing public analysis.
- 2026-06-non-friend-messages-requests-in-uk: no current experiment id or consumer ties UK users to a changed non-friend message-request path 다음 확인: Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, or user-facing string linkage before writing public analysis.
- 2026-06-clips-editor-v2: no current experiment id or config consumer ties Clips editor strings or UI to this experiment 다음 확인: Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, or user-facing string linkage before writing public analysis.
- 2026-06-mobile-server-tag: current guild settings/store module registers the experiment, and server tag strings appeared, but the experiment result is not assigned or read 다음 확인: Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, or user-facing string linkage before writing public analysis.
- 2026-05-quest-tile-cta-refactor: definition/export still exists in the Quest experiment module, but no current helper consumer was confirmed 다음 확인: Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, or user-facing string linkage before writing public analysis.
- 2026-06-polls-click-to-profile: no current experiment id match or poll-click profile consumer found 다음 확인: Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, or user-facing string linkage before writing public analysis.
- 2026-06-game-invites-channel: game and voice/social play strings changed, but no current experiment id or config consumer links them to the guild experiment 다음 확인: Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, or user-facing string linkage before writing public analysis.
- 2026-06-similar-games-desktop: no current experiment id match or similar-games desktop UI/API consumer found 다음 확인: Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, or user-facing string linkage before writing public analysis.
- 2026-06-similar-games-mobile: no current experiment id match or similar-games mobile UI/API consumer found 다음 확인: Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, or user-facing string linkage before writing public analysis.
- 2026-06-wishlist-pdp-gift-button-priority: no current experiment id or gift button priority consumer found 다음 확인: Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, or user-facing string linkage before writing public analysis.
- 2026-06-server-boost-bar-nudge: boost theme strings appeared, but no current experiment id or config consumer links the server Boost bar nudge to a visible surface 다음 확인: Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, or user-facing string linkage before writing public analysis.
- 2026-06-improved-shop-loading: no current experiment id or Shop loading consumer found 다음 확인: Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, or user-facing string linkage before writing public analysis.
- 2026-05-clips-timeline: no current experiment id or Clips timeline consumer found in the current bundle 다음 확인: Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, or user-facing string linkage before writing public analysis.
- 2026-06-orb-redemptions-billing-history: Orbs/Nitro redemption strings changed in-window, but no current experiment id or config consumer ties billing history behavior to this experiment 다음 확인: Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, or user-facing string linkage before writing public analysis.
- 2026-06-game-profile-share-link: current consumer confirms game-profile coded-link analytics tracking, but showSmallEmbed or another user-visible UI consumer was not found 다음 확인: Re-search the current Canary bundle for a concrete showSmallEmbed UI consumer, route, store/action, or user-facing string linkage before writing public analysis.

## 검증 및 커밋/푸시 결과
- JSON 유효성 검사: `history/latest/public web JSON`과 새 report JSON 모두 통과했습니다.
- 금지 fallback 문구 검색과 공개 report 민감 정보 검색은 통과했습니다.
- `git diff --check`를 통과했습니다.
- public data/report 커밋 `1210ab7 Add weekly experiment interpretations`를 생성했고 `origin/main`에 푸시했습니다.
- 이 리포트의 publish 결과 metadata는 후속 커밋 `Record weekly report publish result`로 기록합니다.

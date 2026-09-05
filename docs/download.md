---
title: 下载 FiberArt
description: 下载 FiberArt 自动铺丝软件最新安装包
hide:
  - navigation
  - toc
comments: false
---

# 下载 FiberArt

请选择适合您的版本：**稳定版**经过完整测试，适合日常使用；**测试版**包含最新功能，可能尚不稳定。

<p class="fa-status" id="fa-status">正在获取最新版本信息...</p>

<div class="grid cards" markdown>

- :material-tag-check: **最新稳定版**

    版本 [<span class="fa-version" data-channel="stable">--</span>](user_guides/changelog.md)

    非加密狗授权

    [下载安装包 :material-download:](#){ .md-button .md-button--primary .fa-dl data-channel="stable" data-kind="zenlicense" }

- :material-tag-check: **最新稳定版**

    版本 [<span class="fa-version" data-channel="stable">--</span>](user_guides/changelog.md)

    加密狗授权

    [下载安装包 :material-download:](#){ .md-button .fa-dl data-channel="stable" data-kind="sentinel" }

- :material-tag: **最新测试版** <span class="fa-badge">测试版</span>

    版本 [<span class="fa-version" data-channel="beta">--</span>](user_guides/changelog.md)

    非加密狗授权

    [下载安装包 :material-download:](#){ .md-button .fa-dl data-channel="beta" data-kind="zenlicense" }

- :material-tag: **最新测试版** <span class="fa-badge">测试版</span>

    版本 [<span class="fa-version" data-channel="beta">--</span>](user_guides/changelog.md)

    加密狗授权

    [下载安装包 :material-download:](#){ .md-button .fa-dl data-channel="beta" data-kind="sentinel" }

</div>

<style>
  .fa-status { color: var(--md-default-fg-color--light); }
  .fa-version { color: var(--md-primary-fg-color); font-weight: 600; }
  .md-typeset .grid.cards {
    grid-template-columns: repeat(2, 1fr) !important;
  }
  @media screen and (max-width: 620px) {
    .md-typeset .grid.cards {
      grid-template-columns: 1fr !important;
    }
  }
  .fa-badge {
    display: inline-block;
    font-size: 0.7rem;
    font-weight: 600;
    padding: 1px 8px;
    border-radius: 999px;
    background: #ffb300;
    color: #5a4200;
    vertical-align: middle;
  }
  [data-md-color-scheme="slate"] .fa-badge {
    background: #ffca28;
    color: #3a2d00;
  }
</style>

<script>
(function () {
  var TEXT = {
    error: '获取最新版本信息失败，请稍后重试。',
    passwordPrompt: '请输入今日下载口令：',
    passwordError: '口令不正确，请重试。'
  };

  var statusEl = document.getElementById('fa-status');
  var data = null;

  function dailyPassword() {
    var d = new Date();
    var s = d.getFullYear().toString() +
      ('0' + (d.getMonth() + 1)).slice(-2) +
      ('0' + d.getDate()).slice(-2);
    var n = 0x45d9f3b ^ 0x2a6f31;
    for (var i = 0; i < s.length; i++) {
      n = Math.imul(n ^ s.charCodeAt(i), 0x27d4eb2d);
      n = (n ^ (n >>> 15)) >>> 0;
    }
    n = Math.imul(n ^ (n >>> 16), 0x85ebca6b) >>> 0;
    n = Math.imul(n ^ (n >>> 13), 0xc2b2ae35) >>> 0;
    return String(((n ^ (n >>> 16)) >>> 0) % 1000000).padStart(6, '0');
  }

  function guardedDownload(url) {
    for (;;) {
      var value = window.prompt(TEXT.passwordPrompt);
      if (value === null) return;
      if (value.trim() === dailyPassword()) {
        window.location.href = url;
        return;
      }
      window.alert(TEXT.passwordError);
    }
  }

  document.querySelectorAll('.fa-dl').forEach(function (btn) {
    btn.addEventListener('click', function (event) {
      event.preventDefault();
      var url = btn.getAttribute('data-url');
      if (!url) {
        window.alert(TEXT.error);
        return;
      }
      guardedDownload(url);
    });
  });

  fetch('latest_version.json')
    .then(function (res) {
      if (!res.ok) throw new Error('HTTP ' + res.status);
      return res.json();
    })
    .then(function (json) {
      data = json;
      statusEl.hidden = true;
      document.querySelectorAll('.fa-version').forEach(function (verEl) {
        var ch = data[verEl.getAttribute('data-channel')] || {};
        verEl.textContent = ch.version || '-';
      });
      document.querySelectorAll('.fa-dl').forEach(function (btn) {
        var ch = data[btn.getAttribute('data-channel')] || {};
        var url = ch['download_url_' + btn.getAttribute('data-kind')];
        if (url) btn.setAttribute('data-url', url);
      });
    })
    .catch(function () {
      statusEl.textContent = TEXT.error;
    });
})();
</script>

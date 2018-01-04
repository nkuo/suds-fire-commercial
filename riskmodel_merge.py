





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://assets-cdn.github.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/frameworks-f27d807afb610bf126cbfb9ce429438a328e012239e5a77fc8152b794553dfc0.css" integrity="sha256-8n2AevthC/Emy/uc5ClDijKOASI55ad/yBUreUVT38A=" media="all" rel="stylesheet" />
  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-90814c795d836404981b54444a6ccc23fac2c6b0e1ce875e90784fbd83445bc5.css" integrity="sha256-kIFMeV2DZASYG1RESmzMI/rCxrDhzodekHhPvYNEW8U=" media="all" rel="stylesheet" />
  
  
  
  

  <meta name="viewport" content="width=device-width">
  
  <title>temporal-fire-risk/riskmodel.py at master · mmadaio/temporal-fire-risk</title>
  <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    
    <meta content="https://avatars1.githubusercontent.com/u/5882008?s=400&amp;v=4" property="og:image" /><meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="mmadaio/temporal-fire-risk" property="og:title" /><meta content="https://github.com/mmadaio/temporal-fire-risk" property="og:url" /><meta content="temporal-fire-risk - Takes in real-time civic data to predict property-level fire risk" property="og:description" />

  <link rel="assets" href="https://assets-cdn.github.com/">
  <link rel="web-socket" href="wss://live.github.com/_sockets/VjI6MjM1OTEzNTc3OmRiZDk0YzAxY2Q3NmE3ZDhiZDQwODJhNGI1MDViMzY0YzZjYTc5OTMxZmRlYjhmNGFkZDg5NTk2YWM5NDkyYTE=--6608cdbb247a4e1230249eb10a1272a6b9473645">
  <meta name="pjax-timeout" content="1000">
  <link rel="sudo-modal" href="/sessions/sudo_modal">
  <meta name="request-id" content="B766:2C070:FE3D2A:24AD23E:5A4DB284" data-pjax-transient>
  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

    <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
  <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
  <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">
    <meta name="google-analytics" content="UA-3769691-2">

<meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="https://collector.githubapp.com/github-external/browser_event" name="octolytics-event-url" /><meta content="B766:2C070:FE3D2A:24AD23E:5A4DB284" name="octolytics-dimension-request_id" /><meta content="iad" name="octolytics-dimension-region_edge" /><meta content="iad" name="octolytics-dimension-region_render" /><meta content="20330339" name="octolytics-actor-id" /><meta content="nkuo" name="octolytics-actor-login" /><meta content="382d079f5714653df94e541406585c8da6371ae90260fea439ab9f7b1ea6ea83" name="octolytics-actor-hash" />
<meta content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" name="analytics-location" />




  <meta class="js-ga-set" name="dimension1" content="Logged In">


  

      <meta name="hostname" content="github.com">
  <meta name="user-login" content="nkuo">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="MjUyMmVlYTBlZmEyZDJkNjZhYTZlZDhmZjJiZWJjYTcxZjVkZWJkNjQyMWRkNzk5ZmM4ZjRiZDYyNTUxZGE5Ynx7InJlbW90ZV9hZGRyZXNzIjoiMTA2LjEwNC4xMTQuOTQiLCJyZXF1ZXN0X2lkIjoiQjc2NjoyQzA3MDpGRTNEMkE6MjRBRDIzRTo1QTREQjI4NCIsInRpbWVzdGFtcCI6MTUxNTA0MTQxNSwiaG9zdCI6ImdpdGh1Yi5jb20ifQ==">

    <meta name="enabled-features" content="UNIVERSE_BANNER,FREE_TRIALS">

  <meta name="html-safe-nonce" content="7dd895d1e47d074fa1246325325cb559d4106f50">

  <meta http-equiv="x-pjax-version" content="33fde39efb62989e9022eefd6d69d17a">
  

      <link href="https://github.com/mmadaio/temporal-fire-risk/commits/master.atom" rel="alternate" title="Recent Commits to temporal-fire-risk:master" type="application/atom+xml">

  <meta name="description" content="temporal-fire-risk - Takes in real-time civic data to predict property-level fire risk">
  <meta name="go-import" content="github.com/mmadaio/temporal-fire-risk git https://github.com/mmadaio/temporal-fire-risk.git">

  <meta content="5882008" name="octolytics-dimension-user_id" /><meta content="mmadaio" name="octolytics-dimension-user_login" /><meta content="103858138" name="octolytics-dimension-repository_id" /><meta content="mmadaio/temporal-fire-risk" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="103858138" name="octolytics-dimension-repository_network_root_id" /><meta content="mmadaio/temporal-fire-risk" name="octolytics-dimension-repository_network_root_nwo" /><meta content="false" name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" />


    <link rel="canonical" href="https://github.com/mmadaio/temporal-fire-risk/blob/master/riskmodel.py" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://assets-cdn.github.com/favicon.ico">

<meta name="theme-color" content="#1e2327">


  <meta name="u2f-support" content="true">

  </head>

  <body class="logged-in env-production page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="bg-black text-white p-3 show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    
      



        
<header class="Header  f5" role="banner">
  <div class="d-flex px-3 flex-justify-between container-lg">
    <div class="d-flex flex-justify-between">
      <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <svg aria-hidden="true" class="octicon octicon-mark-github" height="32" version="1.1" viewBox="0 0 16 16" width="32"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>


    </div>

    <div class="HeaderMenu d-flex flex-justify-between flex-auto">
      <div class="d-flex">
            <div class="">
              <div class="header-search scoped-search site-scoped-search js-site-search" role="search">
  <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/mmadaio/temporal-fire-risk/search" class="js-site-search-form" data-scoped-search-url="/mmadaio/temporal-fire-risk/search" data-unscoped-search-url="/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <label class="form-control header-search-wrapper js-chromeless-input-container">
        <a href="/mmadaio/temporal-fire-risk/blob/master/riskmodel.py" class="header-search-scope no-underline">This repository</a>
      <input type="text"
        class="form-control header-search-input js-site-search-focus js-site-search-field is-clearable"
        data-hotkey="s"
        name="q"
        value=""
        placeholder="Search"
        aria-label="Search this repository"
        data-unscoped-placeholder="Search GitHub"
        data-scoped-placeholder="Search"
        autocapitalize="off">
        <input type="hidden" class="js-site-search-type-field" name="type" >
    </label>
</form></div>

            </div>

          <ul class="d-flex pl-2 flex-items-center text-bold list-style-none" role="navigation">
            <li>
              <a href="/pulls" aria-label="Pull requests you created" class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:pulls context:user" data-hotkey="g p" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls">
                Pull requests
</a>            </li>
            <li>
              <a href="/issues" aria-label="Issues you created" class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:issues context:user" data-hotkey="g i" data-selected-links="/issues /issues/assigned /issues/mentioned /issues">
                Issues
</a>            </li>
                <li>
                  <a href="/marketplace" class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:marketplace context:user" data-selected-links=" /marketplace">
                    Marketplace
</a>                </li>
            <li>
              <a href="/explore" class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship showcases showcases_search showcases_landing /explore">
                Explore
</a>            </li>
          </ul>
      </div>

      <div class="d-flex">
        
<ul class="user-nav d-flex flex-items-center list-style-none" id="user-links">
  <li class="dropdown js-menu-container">
    <span class="d-inline-block  px-2">
      

    </span>
  </li>

  <li class="dropdown js-menu-container">
    <details class="dropdown-details details-reset js-dropdown-details d-flex px-2 flex-items-center">
      <summary class="HeaderNavlink"
         aria-label="Create new…"
         data-ga-click="Header, create new, icon:add">
        <svg aria-hidden="true" class="octicon octicon-plus float-left mr-1 mt-1" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 9H7v5H5V9H0V7h5V2h2v5h5z"/></svg>
        <span class="dropdown-caret mt-1"></span>
      </summary>

      <ul class="dropdown-menu dropdown-menu-sw">
        
<a class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>

<a class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, create new gist">
  New gist
</a>

  <a class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>



  <div class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="mmadaio/temporal-fire-risk">This repository</span>
  </div>
    <a class="dropdown-item" href="/mmadaio/temporal-fire-risk/issues/new" data-ga-click="Header, create new issue">
      New issue
    </a>

      </ul>
    </details>
  </li>

  <li class="dropdown js-menu-container">

    <details class="dropdown-details details-reset js-dropdown-details d-flex pl-2 flex-items-center">
      <summary class="HeaderNavlink name mt-1"
        aria-label="View profile and more"
        data-ga-click="Header, show menu, icon:avatar">
        <img alt="@nkuo" class="avatar float-left mr-1" src="https://avatars3.githubusercontent.com/u/20330339?s=40&amp;v=4" height="20" width="20">
        <span class="dropdown-caret"></span>
      </summary>

      <ul class="dropdown-menu dropdown-menu-sw">
        <li class="dropdown-header header-nav-current-user css-truncate">
          Signed in as <strong class="css-truncate-target">nkuo</strong>
        </li>

        <li class="dropdown-divider"></li>

        <li><a class="dropdown-item" href="/nkuo" data-ga-click="Header, go to profile, text:your profile">
          Your profile
        </a></li>
        <li><a class="dropdown-item" href="/nkuo?tab=stars" data-ga-click="Header, go to starred repos, text:your stars">
          Your stars
        </a></li>
          <li><a class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, your gists, text:your gists">Your Gists</a></li>

        <li class="dropdown-divider"></li>

        <li><a class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">
          Help
        </a></li>

        <li><a class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">
          Settings
        </a></li>

        <li><!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/logout" class="logout-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="M07hqQAFuCYTKFMdcCB3QvUpUopEC0Wxx4xYqPK/DNV3J/yK7BvBdvW6GlChSBnBf10YMA28eAEs3CoMb1PWuw==" /></div>
          <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
        </form></li>
      </ul>
    </details>
  </li>
</ul>


        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/logout" class="sr-only right-0" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="haBPBq1CK9g/5qIcL5LPkBfpLFUqeppPQ2eCbp+L+XDByVIlQVxSiNl061H++qETnZ1m72PNp/+oN/DKAmcjHg==" /></div>
          <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
</form>      </div>
    </div>
  </div>
</header>

      

  </div>

  <div id="start-of-content" class="show-on-focus"></div>

    <div id="js-flash-container">
</div>



  <div role="main" >
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <div id="js-repo-pjax-container" data-pjax-container >
      






  <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav  ">
    <div class="repohead-details-container clearfix container">

      <ul class="pagehead-actions">
  <li>
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="+oziM5l7opNPSAKZpkHWCy93+y39iTNU0CfVWO57gkrG4+fK16sPlw4OrTVr1lyLcjcr2/Ouwuq4y8HsKq1U+g==" /></div>      <input class="form-control" id="repository_id" name="repository_id" type="hidden" value="103858138" />

        <div class="select-menu js-menu-container js-select-menu">
          <a href="/mmadaio/temporal-fire-risk/subscription"
            class="btn btn-sm btn-with-count select-menu-button js-menu-target"
            role="button"
            aria-haspopup="true"
            aria-expanded="false"
            aria-label="Toggle repository notifications menu"
            data-ga-click="Repository, click Watch settings, action:blob#show">
            <span class="js-select-button">
                <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                Watch
            </span>
          </a>
          <a class="social-count js-social-count"
            href="/mmadaio/temporal-fire-risk/watchers"
            aria-label="1 user is watching this repository">
            1
          </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content">
            <div class="select-menu-header js-navigation-enable" tabindex="-1">
              <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
              <span class="select-menu-title">Notifications</span>
            </div>

              <div class="select-menu-list js-navigation-container" role="menu">

                <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                    <span class="select-menu-item-heading">Not watching</span>
                    <span class="description">Be notified when participating or @mentioned.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                      Watch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                    <span class="select-menu-item-heading">Watching</span>
                    <span class="description">Be notified of all conversations.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                        Unwatch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input id="do_ignore" name="do" type="radio" value="ignore" />
                    <span class="select-menu-item-heading">Ignoring</span>
                    <span class="description">Never be notified.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-mute" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8 2.81v10.38c0 .67-.81 1-1.28.53L3 10H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h2l3.72-3.72C7.19 1.81 8 2.14 8 2.81zm7.53 3.22l-1.06-1.06-1.97 1.97-1.97-1.97-1.06 1.06L11.44 8 9.47 9.97l1.06 1.06 1.97-1.97 1.97 1.97 1.06-1.06L13.56 8l1.97-1.97z"/></svg>
                        Stop ignoring
                    </span>
                  </div>
                </div>

              </div>

            </div>
          </div>
        </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/mmadaio/temporal-fire-risk/unstar" class="starred js-social-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="eTcUfMIdZGwil7bGeq/26bog03DeaRC4pTnwa8BwT5d03KkS3EnMvsoKVyWpXj3vGkJeISKE4WLP/uOSviHRLg==" /></div>
      <input type="hidden" name="context" value="repository"></input>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar mmadaio/temporal-fire-risk"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/mmadaio/temporal-fire-risk/stargazers"
           aria-label="0 users starred this repository">
          0
        </a>
</form>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/mmadaio/temporal-fire-risk/star" class="unstarred js-social-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="FV5hGbW+YpXFhGTvwc3l+QFB1s5hW9g2mlHO3yMMPqj62LIAcVf/yPlbH31rDc4xGAWRYBCz2gp8Tm+sb7ADqA==" /></div>
      <input type="hidden" name="context" value="repository"></input>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star mmadaio/temporal-fire-risk"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
        Star
      </button>
        <a class="social-count js-social-count" href="/mmadaio/temporal-fire-risk/stargazers"
           aria-label="0 users starred this repository">
          0
        </a>
</form>  </div>

  </li>

  <li>
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/mmadaio/temporal-fire-risk/fork" class="btn-with-count" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="fxcTTgHbwSZbWf1/1jZUqJrscmceio1PBo33U9zJcG9XjHiRiDZpYPXA4bM5pqncmrzNfhe63X232/Hgqfi7dQ==" /></div>
            <button
                type="submit"
                class="btn btn-sm btn-with-count"
                data-ga-click="Repository, show fork modal, action:blob#show; text:Fork"
                title="Fork your own copy of mmadaio/temporal-fire-risk to your account"
                aria-label="Fork your own copy of mmadaio/temporal-fire-risk to your account">
              <svg aria-hidden="true" class="octicon octicon-repo-forked" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
              Fork
            </button>
</form>
    <a href="/mmadaio/temporal-fire-risk/network" class="social-count"
       aria-label="0 users forked this repository">
      0
    </a>
  </li>
</ul>

      <h1 class="public ">
  <svg aria-hidden="true" class="octicon octicon-repo" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a href="/mmadaio" class="url fn" rel="author">mmadaio</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a href="/mmadaio/temporal-fire-risk" data-pjax="#js-repo-pjax-container">temporal-fire-risk</a></strong>

</h1>

    </div>
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax container"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/mmadaio/temporal-fire-risk" class="js-selected-navigation-item selected reponav-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /mmadaio/temporal-fire-risk" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-code" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a href="/mmadaio/temporal-fire-risk/issues" class="js-selected-navigation-item reponav-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /mmadaio/temporal-fire-risk/issues" itemprop="url">
        <svg aria-hidden="true" class="octicon octicon-issue-opened" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="Counter">0</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/mmadaio/temporal-fire-risk/pulls" class="js-selected-navigation-item reponav-item" data-hotkey="g p" data-selected-links="repo_pulls /mmadaio/temporal-fire-risk/pulls" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-git-pull-request" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">0</span>
      <meta itemprop="position" content="3">
</a>  </span>

    <a href="/mmadaio/temporal-fire-risk/projects" class="js-selected-navigation-item reponav-item" data-hotkey="g b" data-selected-links="repo_projects new_repo_project repo_project /mmadaio/temporal-fire-risk/projects">
      <svg aria-hidden="true" class="octicon octicon-project" height="16" version="1.1" viewBox="0 0 15 16" width="15"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      Projects
      <span class="Counter" >0</span>
</a>
    <a href="/mmadaio/temporal-fire-risk/wiki" class="js-selected-navigation-item reponav-item" data-hotkey="g w" data-selected-links="repo_wiki /mmadaio/temporal-fire-risk/wiki">
      <svg aria-hidden="true" class="octicon octicon-book" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M3 5h4v1H3V5zm0 3h4V7H3v1zm0 2h4V9H3v1zm11-5h-4v1h4V5zm0 2h-4v1h4V7zm0 2h-4v1h4V9zm2-6v9c0 .55-.45 1-1 1H9.5l-1 1-1-1H2c-.55 0-1-.45-1-1V3c0-.55.45-1 1-1h5.5l1 1 1-1H15c.55 0 1 .45 1 1zm-8 .5L7.5 3H2v9h6V3.5zm7-.5H9.5l-.5.5V12h6V3z"/></svg>
      Wiki
</a>

  <a href="/mmadaio/temporal-fire-risk/pulse" class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse /mmadaio/temporal-fire-risk/pulse">
    <svg aria-hidden="true" class="octicon octicon-graph" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
    Insights
</a>

</nav>


  </div>

<div class="container new-discussion-timeline experiment-repo-nav ">
  <div class="repository-content ">

    
  <a href="/mmadaio/temporal-fire-risk/blob/2a5756a19023aeb32c5c508403f8bbe9855a3098/riskmodel.py" class="d-none js-permalink-shortcut" data-hotkey="y">Permalink</a>

  <!-- blob contrib key: blob_contributors:v21:1678596b895b89570331a732395f1d30 -->

  <div class="file-navigation js-zeroclipboard-container">
    
<div class="select-menu branch-select-menu js-menu-container js-select-menu float-left">
  <button class=" btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    
    type="button" aria-label="Switch branches or tags" aria-expanded="false" aria-haspopup="true">
      <i>Branch:</i>
      <span class="js-select-button css-truncate-target">master</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/mmadaio/temporal-fire-risk/blob/master/riskmodel.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

    <div class="BtnGroup float-right">
      <a href="/mmadaio/temporal-fire-risk/find/master"
            class="js-pjax-capture-input btn btn-sm BtnGroup-item"
            data-pjax
            data-hotkey="t">
        Find file
      </a>
      <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm BtnGroup-item tooltipped tooltipped-s" data-copied-hint="Copied!" type="button">Copy path</button>
    </div>
    <div class="breadcrumb js-zeroclipboard-target">
      <span class="repo-root js-repo-root"><span class="js-path-segment"><a href="/mmadaio/temporal-fire-risk"><span>temporal-fire-risk</span></a></span></span><span class="separator">/</span><strong class="final-path">riskmodel.py</strong>
    </div>
  </div>


  
  <div class="commit-tease">
      <span class="float-right">
        <a class="commit-tease-sha" href="/mmadaio/temporal-fire-risk/commit/2a5756a19023aeb32c5c508403f8bbe9855a3098" data-pjax>
          2a5756a
        </a>
        <relative-time datetime="2018-01-04T00:19:49Z">Jan 3, 2018</relative-time>
      </span>
      <div>
        <img alt="" class="avatar" data-canonical-src="https://0.gravatar.com/avatar/db604faff8bd1b75885049ca41388aa9?d=https%3A%2F%2Fassets-cdn.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png&amp;r=g&amp;s=140" height="20" src="https://camo.githubusercontent.com/879a40d9df97b4bb84081cb4d1f1e1c61941d80f/68747470733a2f2f302e67726176617461722e636f6d2f6176617461722f64623630346661666638626431623735383835303439636134313338386161393f643d68747470732533412532462532466173736574732d63646e2e6769746875622e636f6d253246696d6167657325324667726176617461727325324667726176617461722d757365722d3432302e706e6726723d6726733d313430" width="20" />
        <span class="user-mention">mmadaio</span>
          <a href="/mmadaio/temporal-fire-risk/commit/2a5756a19023aeb32c5c508403f8bbe9855a3098" class="message" data-pjax="true" title="Update with output logging and image saving">Update with output logging and image saving</a>
      </div>

    <div class="commit-tease-contributors">
      <button type="button" class="btn-link muted-link contributors-toggle" data-facebox="#blob_contributors_box">
        <strong>1</strong>
         contributor
      </button>
      
    </div>

    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header" data-facebox-id="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list" data-facebox-id="facebox-description">
          <li class="facebox-user-list-item">
            <img alt="@mmadaio" height="24" src="https://avatars1.githubusercontent.com/u/5882008?s=48&amp;v=4" width="24" />
            <a href="/mmadaio">mmadaio</a>
          </li>
      </ul>
    </div>
  </div>


  <div class="file">
    <div class="file-header">
  <div class="file-actions">

    <div class="BtnGroup">
      <a href="/mmadaio/temporal-fire-risk/raw/master/riskmodel.py" class="btn btn-sm BtnGroup-item" id="raw-url">Raw</a>
        <a href="/mmadaio/temporal-fire-risk/blame/master/riskmodel.py" class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b">Blame</a>
      <a href="/mmadaio/temporal-fire-risk/commits/master/riskmodel.py" class="btn btn-sm BtnGroup-item" rel="nofollow">History</a>
    </div>


        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/mmadaio/temporal-fire-risk/edit/master/riskmodel.py" class="inline-form js-update-url-with-hash" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="1TYsrN1lFeHoeu+DwsKDLr2mwEJcDXwwydT7dUNRHBTTZWnU+JSThoQl5JAiiNNp54XSPLGiWHnjHZjMWUcEVQ==" /></div>
          <button class="btn-octicon tooltipped tooltipped-nw" type="submit"
            aria-label="Fork this project and edit the file" data-hotkey="e" data-disable-with>
            <svg aria-hidden="true" class="octicon octicon-pencil" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
          </button>
</form>        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/mmadaio/temporal-fire-risk/delete/master/riskmodel.py" class="inline-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="IiFQ9+2XHFhAR6fz6JJ7VNeW9PEtqtY6D8PEV4g1yyItFul6L+MyMLtI2Xe4rj8g5zj4u+yzbhBm1kniwjV31g==" /></div>
          <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit"
            aria-label="Fork this project and delete the file" data-disable-with>
            <svg aria-hidden="true" class="octicon octicon-trashcan" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
          </button>
</form>  </div>

  <div class="file-info">
      <span class="file-mode" title="File mode">executable file</span>
      <span class="file-info-divider"></span>
      578 lines (470 sloc)
      <span class="file-info-divider"></span>
    25.6 KB
  </div>
</div>

    

  <div itemprop="text" class="blob-wrapper data type-python">
      <table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>### Created as part of the Metro21 Fire Risk Analysis project</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>### In partnership with the City of Pittsburgh&#39;s Department of Innovation and Performance, and the Pittsburgh Bureau of Fire</span></td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Authors:</span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>   Bhavkaran Singh</span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>   Michael Madaio</span></td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>   Qianyi Hu</span></td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>   Nathan Kuo</span></td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>   Palak Narang</span></td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>   Jeffrey Chen</span></td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>   Fangyan Chen</span></td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>importing relevant libraries</span></td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> matplotlib</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Force matplotlib to not use any Xwindows backend.</span></td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line">matplotlib.use(<span class="pl-s"><span class="pl-pds">&#39;</span>Agg<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> pandas <span class="pl-k">as</span> pd</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> numpy <span class="pl-k">as</span> np</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> sqlalchemy <span class="pl-k">as</span> sa</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> matplotlib.pyplot <span class="pl-k">as</span> plt</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> sklearn.decomposition <span class="pl-k">import</span> <span class="pl-c1">PCA</span></td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> sklearn.preprocessing <span class="pl-k">import</span> scale</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> pandas <span class="pl-k">as</span> pd</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> sklearn <span class="pl-k">import</span> datasets, linear_model, cross_validation, grid_search</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> numpy <span class="pl-k">as</span> np</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> pandas <span class="pl-k">as</span> pd</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> sklearn.preprocessing <span class="pl-k">import</span> StandardScaler</td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> sklearn.ensemble <span class="pl-k">import</span> RandomForestClassifier</td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> sklearn.cross_validation <span class="pl-k">import</span> KFold, StratifiedKFold, cross_val_score</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> sklearn.pipeline <span class="pl-k">import</span> Pipeline</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> sklearn.linear_model <span class="pl-k">import</span> LogisticRegression</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> sklearn.grid_search <span class="pl-k">import</span> GridSearchCV</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> sklearn_pandas <span class="pl-k">import</span> DataFrameMapper</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> sklearn.preprocessing <span class="pl-k">import</span> OneHotEncoder</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> sklearn <span class="pl-k">import</span> metrics</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> sklearn.metrics <span class="pl-k">import</span> confusion_matrix</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> xgboost <span class="pl-k">import</span> XGBClassifier</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> sklearn.ensemble <span class="pl-k">import</span> ExtraTreesClassifier</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> datetime</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> dateutil.relativedelta <span class="pl-k">import</span> relativedelta</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Turn off pandas chained assignment warning</span></td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line">pd.options.mode.chained_assignment <span class="pl-k">=</span> <span class="pl-c1">None</span>  <span class="pl-c"><span class="pl-c">#</span> default=&#39;warn&#39;</span></td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Reading plidata</span></td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">plidata <span class="pl-k">=</span> pd.read_csv(<span class="pl-s"><span class="pl-pds">&#39;</span>/home/linadmin/FirePred/datasets/pli.csv<span class="pl-pds">&#39;</span></span>,<span class="pl-v">encoding</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>utf-8<span class="pl-pds">&#39;</span></span>,<span class="pl-v">dtype</span><span class="pl-k">=</span>{<span class="pl-s"><span class="pl-pds">&#39;</span>STREET_NUM<span class="pl-pds">&#39;</span></span>:<span class="pl-s"><span class="pl-pds">&#39;</span>str<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>STREET_NAME<span class="pl-pds">&#39;</span></span>:<span class="pl-s"><span class="pl-pds">&#39;</span>str<span class="pl-pds">&#39;</span></span>}, <span class="pl-v">low_memory</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>Reading city of Pittsburgh dataset</span></td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line">pittdata <span class="pl-k">=</span> pd.read_csv(<span class="pl-s"><span class="pl-pds">&#39;</span>/home/linadmin/FirePred/datasets/pittdata.csv<span class="pl-pds">&#39;</span></span>,<span class="pl-v">dtype</span><span class="pl-k">=</span>{<span class="pl-s"><span class="pl-pds">&#39;</span>PROPERTYADDRESS<span class="pl-pds">&#39;</span></span>:<span class="pl-s"><span class="pl-pds">&#39;</span>str<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>PROPERTYHOUSENUM<span class="pl-pds">&#39;</span></span>:<span class="pl-s"><span class="pl-pds">&#39;</span>str<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>CLASSDESC<span class="pl-pds">&#39;</span></span>:<span class="pl-s"><span class="pl-pds">&#39;</span>str<span class="pl-pds">&#39;</span></span>}, <span class="pl-v">low_memory</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>removing extra whitespaces</span></td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line">plidata[<span class="pl-s"><span class="pl-pds">&#39;</span>STREET_NAME<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> plidata[<span class="pl-s"><span class="pl-pds">&#39;</span>STREET_NAME<span class="pl-pds">&#39;</span></span>].str.strip()</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line">plidata[<span class="pl-s"><span class="pl-pds">&#39;</span>STREET_NUM<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> plidata[<span class="pl-s"><span class="pl-pds">&#39;</span>STREET_NUM<span class="pl-pds">&#39;</span></span>].str.strip()</td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>removing residential data</span></td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">pittdata <span class="pl-k">=</span> pittdata[pittdata.<span class="pl-c1">CLASSDESC</span><span class="pl-k">!=</span><span class="pl-s"><span class="pl-pds">&#39;</span>RESIDENTIAL<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line">pittdata <span class="pl-k">=</span> pittdata[pittdata.<span class="pl-c1">PROPERTYHOUSENUM</span><span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>0<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line">pittdata <span class="pl-k">=</span> pittdata[pittdata.<span class="pl-c1">PROPERTYADDRESS</span><span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>dropping columns with less than 15% data</span></td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line">pittdata <span class="pl-k">=</span> pittdata.dropna(<span class="pl-v">thresh</span><span class="pl-k">=</span><span class="pl-c1">4000</span>, <span class="pl-v">axis</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line">pittdata <span class="pl-k">=</span> pittdata.rename(<span class="pl-v">columns</span><span class="pl-k">=</span>{pittdata.columns[<span class="pl-c1">0</span>]:<span class="pl-s"><span class="pl-pds">&#39;</span>PARID<span class="pl-pds">&#39;</span></span>})</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line">pittdata <span class="pl-k">=</span> pittdata.drop_duplicates()</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>merging pli with city of pitt</span></td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">plipca <span class="pl-k">=</span> pd.merge(pittdata, plidata[[<span class="pl-s"><span class="pl-pds">&#39;</span>PARCEL<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>INSPECTION_DATE<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>INSPECTION_RESULT<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>VIOLATION<span class="pl-pds">&#39;</span></span>]], <span class="pl-v">how</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>left<span class="pl-pds">&#39;</span></span>, <span class="pl-v">left_on</span> <span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>PARID<span class="pl-pds">&#39;</span></span>], <span class="pl-v">right_on</span> <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>PARCEL<span class="pl-pds">&#39;</span></span>] )</td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line">plipca <span class="pl-k">=</span> plipca.drop_duplicates()</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>dropping nas</span></td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line">newpli <span class="pl-k">=</span> plipca.dropna(<span class="pl-v">subset</span> <span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>PARCEL<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>INSPECTION_DATE<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>INSPECTION_RESULT<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>VIOLATION<span class="pl-pds">&#39;</span></span>] )</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">newpli <span class="pl-k">=</span> newpli.reset_index()</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line">newpli <span class="pl-k">=</span> newpli.drop([<span class="pl-s"><span class="pl-pds">&#39;</span>index<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>PARID<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>index<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>PROPERTYCITY<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>PROPERTYSTATE<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>PROPERTYUNIT<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>PROPERTYZIP<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>MUNICODE<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>MUNIDESC<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>SCHOOLCODE<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>SCHOOLDESC<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>LEGAL1<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>LEGAL2<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>LEGAL3<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>NEIGHCODE<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>TAXCODE<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>TAXDESC<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>OWNERCODE<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>OWNERDESC<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>CLASS<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>CLASSDESC<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>USECODE<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>USEDESC<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>LOTAREA<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>SALEDATE<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>SALEPRICE<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>SALECODE<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>SALEDESC<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>DEEDBOOK<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>DEEDPAGE<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>CHANGENOTICEADDRESS1<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>CHANGENOTICEADDRESS2<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>CHANGENOTICEADDRESS3<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>CHANGENOTICEADDRESS4<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>COUNTYBUILDING<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>COUNTYLAND<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>COUNTYTOTAL<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>COUNTYEXEMPTBLDG<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>LOCALBUILDING<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>LOCALLAND<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>LOCALTOTAL<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>FAIRMARKETBUILDING<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>FAIRMARKETLAND<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>FAIRMARKETTOTAL<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&#39;</span>PARCEL<span class="pl-pds">&#39;</span></span>], <span class="pl-v">axis</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">newpli <span class="pl-k">=</span> newpli.drop_duplicates()</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>converting to datetime</span></td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">newpli.<span class="pl-c1">INSPECTION_DATE</span> <span class="pl-k">=</span> pd.to_datetime(newpli.<span class="pl-c1">INSPECTION_DATE</span>)</td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">newpli[<span class="pl-s"><span class="pl-pds">&#39;</span>violation_year<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> newpli[<span class="pl-s"><span class="pl-pds">&#39;</span>INSPECTION_DATE<span class="pl-pds">&#39;</span></span>].map(<span class="pl-k">lambda</span> <span class="pl-smi">x</span>: x.year)</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">plipca.<span class="pl-c1">SALEPRICE</span> <span class="pl-k">=</span> plipca.<span class="pl-c1">SALEPRICE</span>.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>NaN<span class="pl-pds">&#39;</span></span>,<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>Groups by address and replaces LOTAREA&#39;,&#39;SALEPRICE&#39;,&#39;FAIRMARKETLAND&#39;,&#39;FAIRMARKETBUILDING&#39; by mean</span></td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">numerical <span class="pl-k">=</span> plipca.groupby( [ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>] , <span class="pl-v">as_index</span><span class="pl-k">=</span><span class="pl-c1">False</span>)[[<span class="pl-s"><span class="pl-pds">&#39;</span>LOTAREA<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>SALEPRICE<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>FAIRMARKETLAND<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>FAIRMARKETBUILDING<span class="pl-pds">&#39;</span></span>]].mean()</td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Following blocks of code group by address and get the category with maximum count for each given categorical columns</span></td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">temp <span class="pl-k">=</span> pd.DataFrame({<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span> : plipca.groupby( [ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>] ).<span class="pl-c1">CLASSDESC</span>.value_counts()}).reset_index()</td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">idx <span class="pl-k">=</span> temp.groupby([ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>])[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>].transform(<span class="pl-c1">max</span>) <span class="pl-k">==</span> temp[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">result1 <span class="pl-k">=</span> temp[idx]</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">result1 <span class="pl-k">=</span> result1.drop_duplicates(<span class="pl-v">subset</span><span class="pl-k">=</span>[ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>], <span class="pl-v">keep</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>last<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> result1[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">temp <span class="pl-k">=</span> pd.DataFrame({<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span> : plipca.groupby( [ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>] ).<span class="pl-c1">CLASSDESC</span>.value_counts()}).reset_index()</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">temp.groupby([ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>])[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>].transform(<span class="pl-c1">max</span>)</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">idx <span class="pl-k">=</span> temp.groupby([ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>])[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>].transform(<span class="pl-c1">max</span>) <span class="pl-k">==</span> temp[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">result1 <span class="pl-k">=</span> temp[idx]</td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">result1 <span class="pl-k">=</span> result1.drop_duplicates(<span class="pl-v">subset</span><span class="pl-k">=</span>[ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>], <span class="pl-v">keep</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>last<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> result1[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">temp <span class="pl-k">=</span> pd.DataFrame({<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span> : plipca.groupby( [ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>] ).<span class="pl-c1">SCHOOLDESC</span>.value_counts()}).reset_index()</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">idx <span class="pl-k">=</span> temp.groupby([ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>])[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>].transform(<span class="pl-c1">max</span>) <span class="pl-k">==</span> temp[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">result2 <span class="pl-k">=</span> temp[idx]</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">result2 <span class="pl-k">=</span> result2.drop_duplicates(<span class="pl-v">subset</span><span class="pl-k">=</span>[ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>], <span class="pl-v">keep</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>last<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> result2[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">temp <span class="pl-k">=</span> pd.DataFrame({<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span> : plipca.groupby( [ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>] ).<span class="pl-c1">OWNERDESC</span>.value_counts()}).reset_index()</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">idx <span class="pl-k">=</span> temp.groupby([ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>])[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>].transform(<span class="pl-c1">max</span>) <span class="pl-k">==</span> temp[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">result3 <span class="pl-k">=</span> temp[idx]</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">result3 <span class="pl-k">=</span> result3.drop_duplicates(<span class="pl-v">subset</span><span class="pl-k">=</span>[ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>], <span class="pl-v">keep</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>last<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> result3[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line">temp <span class="pl-k">=</span> pd.DataFrame({<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span> : plipca.groupby( [ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>] ).<span class="pl-c1">MUNIDESC</span>.value_counts()}).reset_index()</td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">idx <span class="pl-k">=</span> temp.groupby([ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>])[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>].transform(<span class="pl-c1">max</span>) <span class="pl-k">==</span> temp[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line">result4 <span class="pl-k">=</span> temp[idx]</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">result4 <span class="pl-k">=</span> result4.drop_duplicates(<span class="pl-v">subset</span><span class="pl-k">=</span>[ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>], <span class="pl-v">keep</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>last<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> result4[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">temp <span class="pl-k">=</span> pd.DataFrame({<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span> : plipca.groupby( [ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>] ).<span class="pl-c1">INSPECTION_RESULT</span>.value_counts()}).reset_index()</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line">idx <span class="pl-k">=</span> temp.groupby([ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>])[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>].transform(<span class="pl-c1">max</span>) <span class="pl-k">==</span> temp[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line">result5 <span class="pl-k">=</span> temp[idx]</td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line">result5 <span class="pl-k">=</span> result5.drop_duplicates(<span class="pl-v">subset</span><span class="pl-k">=</span>[ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>], <span class="pl-v">keep</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>last<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> result5[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line">temp <span class="pl-k">=</span> pd.DataFrame({<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span> : plipca.groupby( [ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>] ).<span class="pl-c1">NEIGHCODE</span>.value_counts()}).reset_index()</td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">idx <span class="pl-k">=</span> temp.groupby([ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>])[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>].transform(<span class="pl-c1">max</span>) <span class="pl-k">==</span> temp[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">result6 <span class="pl-k">=</span> temp[idx]</td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">result6 <span class="pl-k">=</span> result6.drop_duplicates(<span class="pl-v">subset</span><span class="pl-k">=</span>[ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>], <span class="pl-v">keep</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>last<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> result6[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">temp <span class="pl-k">=</span> pd.DataFrame({<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span> : plipca.groupby( [ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>] ).<span class="pl-c1">TAXDESC</span>.value_counts()}).reset_index()</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">idx <span class="pl-k">=</span> temp.groupby([ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>])[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>].transform(<span class="pl-c1">max</span>) <span class="pl-k">==</span> temp[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line">result7 <span class="pl-k">=</span> temp[idx]</td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line">result7 <span class="pl-k">=</span> result7.drop_duplicates(<span class="pl-v">subset</span><span class="pl-k">=</span>[ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>], <span class="pl-v">keep</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>last<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> result7[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">temp <span class="pl-k">=</span> pd.DataFrame({<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span> : plipca.groupby( [ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>] ).<span class="pl-c1">USEDESC</span>.value_counts()}).reset_index()</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">idx <span class="pl-k">=</span> temp.groupby([ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>])[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>].transform(<span class="pl-c1">max</span>) <span class="pl-k">==</span> temp[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">result8 <span class="pl-k">=</span> temp[idx]</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">result8 <span class="pl-k">=</span> result8.drop_duplicates(<span class="pl-v">subset</span><span class="pl-k">=</span>[ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>], <span class="pl-v">keep</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>last<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> result8[<span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line">dfs <span class="pl-k">=</span> [result1,result2,result3,result4,result6,result7,result8,numerical]</td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line">pcafinal <span class="pl-k">=</span> <span class="pl-v">reduce</span>(<span class="pl-k">lambda</span> <span class="pl-smi">left</span>,<span class="pl-smi">right</span>: pd.merge(left,right,<span class="pl-v">on</span><span class="pl-k">=</span> [ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>] ), dfs)</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line">plipca1 <span class="pl-k">=</span> pd.merge(pcafinal, newpli, <span class="pl-v">how</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>left<span class="pl-pds">&#39;</span></span>, <span class="pl-v">left_on</span> <span class="pl-k">=</span>[ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>], <span class="pl-v">right_on</span> <span class="pl-k">=</span> [ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>] )</td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>loading fire incidents csvs</span></td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line">fire_pre14 <span class="pl-k">=</span> pd.read_csv(<span class="pl-s"><span class="pl-pds">&#39;</span>/home/linadmin/FirePred/datasets/Fire_Incidents_Pre14.csv<span class="pl-pds">&#39;</span></span>,<span class="pl-v">encoding</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>latin-1<span class="pl-pds">&#39;</span></span>,<span class="pl-v">dtype</span><span class="pl-k">=</span>{<span class="pl-s"><span class="pl-pds">&#39;</span>street<span class="pl-pds">&#39;</span></span>:<span class="pl-s"><span class="pl-pds">&#39;</span>str<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>number<span class="pl-pds">&#39;</span></span>:<span class="pl-s"><span class="pl-pds">&#39;</span>str<span class="pl-pds">&#39;</span></span>}, <span class="pl-v">low_memory</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>cleaning columns of fire_pre14</span></td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line">fire_pre14[<span class="pl-s"><span class="pl-pds">&#39;</span>full.code<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> fire_pre14[<span class="pl-s"><span class="pl-pds">&#39;</span>full.code<span class="pl-pds">&#39;</span></span>].str.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>  -<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span> -<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">fire_pre14[<span class="pl-s"><span class="pl-pds">&#39;</span>st_type<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> fire_pre14[<span class="pl-s"><span class="pl-pds">&#39;</span>st_type<span class="pl-pds">&#39;</span></span>].str.strip()</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">fire_pre14[<span class="pl-s"><span class="pl-pds">&#39;</span>street<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> fire_pre14[<span class="pl-s"><span class="pl-pds">&#39;</span>street<span class="pl-pds">&#39;</span></span>].str.strip()</td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line">fire_pre14[<span class="pl-s"><span class="pl-pds">&#39;</span>number<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> fire_pre14[<span class="pl-s"><span class="pl-pds">&#39;</span>number<span class="pl-pds">&#39;</span></span>].str.strip()</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line">fire_pre14[<span class="pl-s"><span class="pl-pds">&#39;</span>st_type<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> fire_pre14[<span class="pl-s"><span class="pl-pds">&#39;</span>st_type<span class="pl-pds">&#39;</span></span>].str.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>AV<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>AVE<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line">fire_pre14[<span class="pl-s"><span class="pl-pds">&#39;</span>street<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> fire_pre14[<span class="pl-s"><span class="pl-pds">&#39;</span>street<span class="pl-pds">&#39;</span></span>].str.strip() <span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span>fire_pre14[<span class="pl-s"><span class="pl-pds">&#39;</span>st_type<span class="pl-pds">&#39;</span></span>].str.strip()</td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>reading the fire_historicalfile</span></td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> pd.read_csv(<span class="pl-s"><span class="pl-pds">&#39;</span>/home/linadmin/FirePred/datasets/Fire_Incidents_New.csv<span class="pl-pds">&#39;</span></span>,<span class="pl-v">encoding</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>utf-8<span class="pl-pds">&#39;</span></span>,<span class="pl-v">dtype</span><span class="pl-k">=</span>{<span class="pl-s"><span class="pl-pds">&#39;</span>street<span class="pl-pds">&#39;</span></span>:<span class="pl-s"><span class="pl-pds">&#39;</span>str<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>number<span class="pl-pds">&#39;</span></span>:<span class="pl-s"><span class="pl-pds">&#39;</span>str<span class="pl-pds">&#39;</span></span>}, <span class="pl-v">low_memory</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>deleting columns not required</span></td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>alm_dttm<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>arv_dttm<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>XCOORD<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>YCOORD<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>alarms<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>inci_type<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>CALL_NO<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> fire_pre14[<span class="pl-s"><span class="pl-pds">&#39;</span>PRIMARY_UNIT<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> fire_pre14[<span class="pl-s"><span class="pl-pds">&#39;</span>MAP_PAGE<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> fire_pre14[<span class="pl-s"><span class="pl-pds">&#39;</span>alm_dttm<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> fire_pre14[<span class="pl-s"><span class="pl-pds">&#39;</span>arv_dttm<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> fire_pre14[<span class="pl-s"><span class="pl-pds">&#39;</span>XCOORD<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> fire_pre14[<span class="pl-s"><span class="pl-pds">&#39;</span>YCOORD<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> fire_pre14[<span class="pl-s"><span class="pl-pds">&#39;</span>inci_id<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> fire_pre14[<span class="pl-s"><span class="pl-pds">&#39;</span>inci_type<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> fire_pre14[<span class="pl-s"><span class="pl-pds">&#39;</span>alarms<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> fire_pre14[<span class="pl-s"><span class="pl-pds">&#39;</span>st_prefix<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> fire_pre14[<span class="pl-s"><span class="pl-pds">&#39;</span>st_suffix<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> fire_pre14[<span class="pl-s"><span class="pl-pds">&#39;</span>st_type<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> fire_pre14[<span class="pl-s"><span class="pl-pds">&#39;</span>CALL_NO<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code blob-code-inner js-file-line">cols <span class="pl-k">=</span> [<span class="pl-c1">0</span>,<span class="pl-c1">4</span>]</td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code blob-code-inner js-file-line">fire_pre14.drop(fire_pre14.columns[cols],<span class="pl-v">axis</span><span class="pl-k">=</span><span class="pl-c1">1</span>,<span class="pl-v">inplace</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>joining both the fire incidents file together</span></td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new.append(fire_pre14, <span class="pl-v">ignore_index</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>more cleaning and removing descriptions which are not fire related</span></td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code blob-code-inner js-file-line">fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>descript<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>descript<span class="pl-pds">&#39;</span></span>].str.strip()</td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>System malfunction, Other<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> fire_new = fire_new[fire_new.descript != &#39;Smoke detector activation, no fire - unintentional&#39;]</span></td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> fire_new = fire_new[fire_new.descript != &#39;Alarm system activation, no fire - unintentional&#39;]</span></td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Detector activation, no fire - unintentional<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Smoke detector activation due to malfunction<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Dispatched &amp; cancelled en route<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Dispatched &amp; cancelled on arrival<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>EMS call, excluding vehicle accident with injury<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Medical assist, assist EMS crew<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Emergency medical service, other<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Good intent call, Other<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Rescue, EMS incident, other<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Medical Alarm Activation (No Medical Service Req)<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Motor Vehicle Accident with no injuries<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>No Incident found on arrival at dispatch address<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Unintentional transmission of alarm, Other<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Motor vehicle accident with injuries<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Vehicle accident, general cleanup<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Power line down<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Person in distress, Other<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Cable/Telco Wires Down<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Service Call, other<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Vehicle Accident canceled en route<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Lock-out<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>False alarm or false call, Other<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Assist police or other governmental agency<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Special type of incident, Other<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Alarm system sounded due to malfunction<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Motor vehicle/pedestrian accident (MV Ped)<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Assist invalid <span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Malicious, mischievous false call, Other<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Accident, potential accident, Other<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Assist invalid<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>EMS call, party transported by non-fire agency<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Rescue or EMS standby<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Public service assistance, Other<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Police matter<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Lock-in (if lock out , use 511 )<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Sprinkler activation, no fire - unintentional<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Wrong location<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Local alarm system, malicious false alarm<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Authorized controlled burning<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="LC252" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Water problem, Other<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L253" class="blob-num js-line-number" data-line-number="253"></td>
        <td id="LC253" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> fire_new = fire_new[fire_new.descript != &#39;Smoke or odor removal&#39;]</span></td>
      </tr>
      <tr>
        <td id="L254" class="blob-num js-line-number" data-line-number="254"></td>
        <td id="LC254" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Passenger vehicle fire<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L255" class="blob-num js-line-number" data-line-number="255"></td>
        <td id="LC255" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>CO detector activation due to malfunction<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L256" class="blob-num js-line-number" data-line-number="256"></td>
        <td id="LC256" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Authorized controlled burning<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L257" class="blob-num js-line-number" data-line-number="257"></td>
        <td id="LC257" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Steam, vapor, fog or dust thought to be smoke<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L258" class="blob-num js-line-number" data-line-number="258"></td>
        <td id="LC258" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Overheated motor<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L259" class="blob-num js-line-number" data-line-number="259"></td>
        <td id="LC259" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Local alarm system, malicious false alarm<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L260" class="blob-num js-line-number" data-line-number="260"></td>
        <td id="LC260" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Central station, malicious false alarm<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L261" class="blob-num js-line-number" data-line-number="261"></td>
        <td id="LC261" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Public service<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L262" class="blob-num js-line-number" data-line-number="262"></td>
        <td id="LC262" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> fire_new = fire_new[fire_new.descript != &#39;Building or structure weakened or collapsed&#39;]</span></td>
      </tr>
      <tr>
        <td id="L263" class="blob-num js-line-number" data-line-number="263"></td>
        <td id="LC263" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Heat detector activation due to malfunction<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L264" class="blob-num js-line-number" data-line-number="264"></td>
        <td id="LC264" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Citizen complaint<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L265" class="blob-num js-line-number" data-line-number="265"></td>
        <td id="LC265" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Municipal alarm system, malicious false alarm<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L266" class="blob-num js-line-number" data-line-number="266"></td>
        <td id="LC266" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Sprinkler activation due to malfunction<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L267" class="blob-num js-line-number" data-line-number="267"></td>
        <td id="LC267" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Severe weather or natural disaster, Other<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L268" class="blob-num js-line-number" data-line-number="268"></td>
        <td id="LC268" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Water evacuation<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L269" class="blob-num js-line-number" data-line-number="269"></td>
        <td id="LC269" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Breakdown of light ballast<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L270" class="blob-num js-line-number" data-line-number="270"></td>
        <td id="LC270" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Extrication of victim(s) from vehicle<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L271" class="blob-num js-line-number" data-line-number="271"></td>
        <td id="LC271" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Flood assessment<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L272" class="blob-num js-line-number" data-line-number="272"></td>
        <td id="LC272" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Telephone, malicious false alarm<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L273" class="blob-num js-line-number" data-line-number="273"></td>
        <td id="LC273" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Cover assignment, standby, moveup<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L274" class="blob-num js-line-number" data-line-number="274"></td>
        <td id="LC274" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new.descript <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Road freight or transport vehicle fire<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L275" class="blob-num js-line-number" data-line-number="275"></td>
        <td id="LC275" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>full.code<span class="pl-pds">&#39;</span></span>].str.strip()  <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>540 - Animal problem, Other<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L276" class="blob-num js-line-number" data-line-number="276"></td>
        <td id="LC276" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>full.code<span class="pl-pds">&#39;</span></span>].str.strip()  <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>5532 - Public Education (Station Visit)<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L277" class="blob-num js-line-number" data-line-number="277"></td>
        <td id="LC277" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new[fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>full.code<span class="pl-pds">&#39;</span></span>].str.strip()  <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>353 - Removal of victim(s) from stalled elevator<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L278" class="blob-num js-line-number" data-line-number="278"></td>
        <td id="LC278" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L279" class="blob-num js-line-number" data-line-number="279"></td>
        <td id="LC279" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>correcting problems with the street column</span></td>
      </tr>
      <tr>
        <td id="L280" class="blob-num js-line-number" data-line-number="280"></td>
        <td id="LC280" class="blob-code blob-code-inner js-file-line">fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>street<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>street<span class="pl-pds">&#39;</span></span>].replace(<span class="pl-v">to_replace</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>, PGH<span class="pl-pds">&#39;</span></span>, <span class="pl-v">value</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">regex</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L281" class="blob-num js-line-number" data-line-number="281"></td>
        <td id="LC281" class="blob-code blob-code-inner js-file-line">fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>street<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>street<span class="pl-pds">&#39;</span></span>].replace(<span class="pl-v">to_replace</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>, P<span class="pl-pds">&#39;</span></span>, <span class="pl-v">value</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">regex</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L282" class="blob-num js-line-number" data-line-number="282"></td>
        <td id="LC282" class="blob-code blob-code-inner js-file-line">fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>street<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>street<span class="pl-pds">&#39;</span></span>].replace(<span class="pl-v">to_replace</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>, <span class="pl-v">value</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">regex</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L283" class="blob-num js-line-number" data-line-number="283"></td>
        <td id="LC283" class="blob-code blob-code-inner js-file-line">fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>street<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>street<span class="pl-pds">&#39;</span></span>].replace(<span class="pl-v">to_replace</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>#.*<span class="pl-pds">&#39;</span></span>, <span class="pl-v">value</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">regex</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L284" class="blob-num js-line-number" data-line-number="284"></td>
        <td id="LC284" class="blob-code blob-code-inner js-file-line">fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>street<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>street<span class="pl-pds">&#39;</span></span>].str.strip()</td>
      </tr>
      <tr>
        <td id="L285" class="blob-num js-line-number" data-line-number="285"></td>
        <td id="LC285" class="blob-code blob-code-inner js-file-line">fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>number<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>number<span class="pl-pds">&#39;</span></span>].str.strip()</td>
      </tr>
      <tr>
        <td id="L286" class="blob-num js-line-number" data-line-number="286"></td>
        <td id="LC286" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L287" class="blob-num js-line-number" data-line-number="287"></td>
        <td id="LC287" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>converting to date time and extracting year</span></td>
      </tr>
      <tr>
        <td id="L288" class="blob-num js-line-number" data-line-number="288"></td>
        <td id="LC288" class="blob-code blob-code-inner js-file-line">fireDate, fireTime <span class="pl-k">=</span> fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>CALL_CREATED_DATE<span class="pl-pds">&#39;</span></span>].str.split(<span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>, <span class="pl-c1">1</span>).str</td>
      </tr>
      <tr>
        <td id="L289" class="blob-num js-line-number" data-line-number="289"></td>
        <td id="LC289" class="blob-code blob-code-inner js-file-line">fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>CALL_CREATED_DATE<span class="pl-pds">&#39;</span></span>]<span class="pl-k">=</span> fireDate</td>
      </tr>
      <tr>
        <td id="L290" class="blob-num js-line-number" data-line-number="290"></td>
        <td id="LC290" class="blob-code blob-code-inner js-file-line">fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>CALL_CREATED_DATE<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> pd.to_datetime(fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>CALL_CREATED_DATE<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L291" class="blob-num js-line-number" data-line-number="291"></td>
        <td id="LC291" class="blob-code blob-code-inner js-file-line">fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>fire_year<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>CALL_CREATED_DATE<span class="pl-pds">&#39;</span></span>].map(<span class="pl-k">lambda</span> <span class="pl-smi">x</span>: x.year)</td>
      </tr>
      <tr>
        <td id="L292" class="blob-num js-line-number" data-line-number="292"></td>
        <td id="LC292" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L293" class="blob-num js-line-number" data-line-number="293"></td>
        <td id="LC293" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>removing all codes with less than 20 occurences</span></td>
      </tr>
      <tr>
        <td id="L294" class="blob-num js-line-number" data-line-number="294"></td>
        <td id="LC294" class="blob-code blob-code-inner js-file-line"><span class="pl-k">for</span> col,val <span class="pl-k">in</span> fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>full.code<span class="pl-pds">&#39;</span></span>].value_counts().iteritems():</td>
      </tr>
      <tr>
        <td id="L295" class="blob-num js-line-number" data-line-number="295"></td>
        <td id="LC295" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> val <span class="pl-k">&lt;</span><span class="pl-c1">20</span> <span class="pl-k">and</span> col[<span class="pl-c1">0</span>]<span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>1<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L296" class="blob-num js-line-number" data-line-number="296"></td>
        <td id="LC296" class="blob-code blob-code-inner js-file-line">        fire_new <span class="pl-k">=</span> fire_new[fire_new[<span class="pl-s"><span class="pl-pds">&#39;</span>full.code<span class="pl-pds">&#39;</span></span>] <span class="pl-k">!=</span> col]</td>
      </tr>
      <tr>
        <td id="L297" class="blob-num js-line-number" data-line-number="297"></td>
        <td id="LC297" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L298" class="blob-num js-line-number" data-line-number="298"></td>
        <td id="LC298" class="blob-code blob-code-inner js-file-line">fire_new <span class="pl-k">=</span> fire_new.drop_duplicates()</td>
      </tr>
      <tr>
        <td id="L299" class="blob-num js-line-number" data-line-number="299"></td>
        <td id="LC299" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L300" class="blob-num js-line-number" data-line-number="300"></td>
        <td id="LC300" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>joining plipca with fireincidents</span></td>
      </tr>
      <tr>
        <td id="L301" class="blob-num js-line-number" data-line-number="301"></td>
        <td id="LC301" class="blob-code blob-code-inner js-file-line">pcafire <span class="pl-k">=</span> pd.merge(plipca1, fire_new, <span class="pl-v">how</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>left<span class="pl-pds">&#39;</span></span>, <span class="pl-v">left_on</span> <span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>PROPERTYADDRESS<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>PROPERTYHOUSENUM<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L302" class="blob-num js-line-number" data-line-number="302"></td>
        <td id="LC302" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">right_on</span> <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>street<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>number<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L303" class="blob-num js-line-number" data-line-number="303"></td>
        <td id="LC303" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L304" class="blob-num js-line-number" data-line-number="304"></td>
        <td id="LC304" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> making the fire column with all type 100s as fires</span></td>
      </tr>
      <tr>
        <td id="L305" class="blob-num js-line-number" data-line-number="305"></td>
        <td id="LC305" class="blob-code blob-code-inner js-file-line">pcafire[<span class="pl-s"><span class="pl-pds">&#39;</span>fire<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> pcafire[<span class="pl-s"><span class="pl-pds">&#39;</span>full.code<span class="pl-pds">&#39;</span></span>].astype(<span class="pl-c1">str</span>).str[<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L306" class="blob-num js-line-number" data-line-number="306"></td>
        <td id="LC306" class="blob-code blob-code-inner js-file-line">pcafire.loc[pcafire.fire <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>1<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>fire<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>fire<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L307" class="blob-num js-line-number" data-line-number="307"></td>
        <td id="LC307" class="blob-code blob-code-inner js-file-line">pcafire.loc[pcafire.fire <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>fire<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>fire<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>No fire<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L308" class="blob-num js-line-number" data-line-number="308"></td>
        <td id="LC308" class="blob-code blob-code-inner js-file-line">pcafire[<span class="pl-s"><span class="pl-pds">&#39;</span>full.code<span class="pl-pds">&#39;</span></span>][pcafire[<span class="pl-s"><span class="pl-pds">&#39;</span>fire<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>fire<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L309" class="blob-num js-line-number" data-line-number="309"></td>
        <td id="LC309" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L310" class="blob-num js-line-number" data-line-number="310"></td>
        <td id="LC310" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>Fire occured after inspection</span></td>
      </tr>
      <tr>
        <td id="L311" class="blob-num js-line-number" data-line-number="311"></td>
        <td id="LC311" class="blob-code blob-code-inner js-file-line">pcafire1 <span class="pl-k">=</span> pcafire[(pcafire.<span class="pl-c1">CALL_CREATED_DATE</span> <span class="pl-k">&gt;=</span> pcafire.<span class="pl-c1">INSPECTION_DATE</span> )]</td>
      </tr>
      <tr>
        <td id="L312" class="blob-num js-line-number" data-line-number="312"></td>
        <td id="LC312" class="blob-code blob-code-inner js-file-line">pcafire1 <span class="pl-k">=</span> pcafire[(pcafire.<span class="pl-c1">CALL_CREATED_DATE</span> <span class="pl-k">&gt;=</span> pcafire.<span class="pl-c1">INSPECTION_DATE</span> )]</td>
      </tr>
      <tr>
        <td id="L313" class="blob-num js-line-number" data-line-number="313"></td>
        <td id="LC313" class="blob-code blob-code-inner js-file-line">pcafire1 <span class="pl-k">=</span> pcafire1[pd.notnull(pcafire1.<span class="pl-c1">INSPECTION_DATE</span>)]</td>
      </tr>
      <tr>
        <td id="L314" class="blob-num js-line-number" data-line-number="314"></td>
        <td id="LC314" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L315" class="blob-num js-line-number" data-line-number="315"></td>
        <td id="LC315" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>checking if violation is in the same year as the fire and keeping only those</span></td>
      </tr>
      <tr>
        <td id="L316" class="blob-num js-line-number" data-line-number="316"></td>
        <td id="LC316" class="blob-code blob-code-inner js-file-line">pcafire2 <span class="pl-k">=</span> pcafire1[(pcafire1.violation_year <span class="pl-k">==</span> pcafire1.fire_year)]</td>
      </tr>
      <tr>
        <td id="L317" class="blob-num js-line-number" data-line-number="317"></td>
        <td id="LC317" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L318" class="blob-num js-line-number" data-line-number="318"></td>
        <td id="LC318" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>joining all rows with no pli violations</span></td>
      </tr>
      <tr>
        <td id="L319" class="blob-num js-line-number" data-line-number="319"></td>
        <td id="LC319" class="blob-code blob-code-inner js-file-line">fire_nopli <span class="pl-k">=</span> pd.concat([fire_new, pcafire2[[<span class="pl-s"><span class="pl-pds">&#39;</span>number<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>street<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>CALL_CREATED_DATE<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>full.code<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>response_time<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>fire_year<span class="pl-pds">&#39;</span></span>]], pcafire2[[<span class="pl-s"><span class="pl-pds">&#39;</span>number<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>street<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>CALL_CREATED_DATE<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>full.code<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>response_time<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>fire_year<span class="pl-pds">&#39;</span></span>]]]).drop_duplicates(<span class="pl-v">keep</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L320" class="blob-num js-line-number" data-line-number="320"></td>
        <td id="LC320" class="blob-code blob-code-inner js-file-line">pcafire_nopli <span class="pl-k">=</span> pd.merge(pcafinal, fire_nopli, <span class="pl-v">how</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>left<span class="pl-pds">&#39;</span></span>, <span class="pl-v">left_on</span> <span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>PROPERTYADDRESS<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>PROPERTYHOUSENUM<span class="pl-pds">&#39;</span></span>],</td>
      </tr>
      <tr>
        <td id="L321" class="blob-num js-line-number" data-line-number="321"></td>
        <td id="LC321" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">right_on</span> <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>street<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>number<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L322" class="blob-num js-line-number" data-line-number="322"></td>
        <td id="LC322" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L323" class="blob-num js-line-number" data-line-number="323"></td>
        <td id="LC323" class="blob-code blob-code-inner js-file-line">pcafire_nopli[<span class="pl-s"><span class="pl-pds">&#39;</span>fire<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> pcafire_nopli[<span class="pl-s"><span class="pl-pds">&#39;</span>full.code<span class="pl-pds">&#39;</span></span>].astype(<span class="pl-c1">str</span>).str[<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L324" class="blob-num js-line-number" data-line-number="324"></td>
        <td id="LC324" class="blob-code blob-code-inner js-file-line">pcafire_nopli.loc[pcafire_nopli.fire <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>1<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>fire<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>fire<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L325" class="blob-num js-line-number" data-line-number="325"></td>
        <td id="LC325" class="blob-code blob-code-inner js-file-line">pcafire_nopli.loc[pcafire_nopli.fire <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>fire<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>fire<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>No fire<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L326" class="blob-num js-line-number" data-line-number="326"></td>
        <td id="LC326" class="blob-code blob-code-inner js-file-line">pcafire_nopli[<span class="pl-s"><span class="pl-pds">&#39;</span>full.code<span class="pl-pds">&#39;</span></span>][pcafire_nopli[<span class="pl-s"><span class="pl-pds">&#39;</span>fire<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>fire<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L327" class="blob-num js-line-number" data-line-number="327"></td>
        <td id="LC327" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L328" class="blob-num js-line-number" data-line-number="328"></td>
        <td id="LC328" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>combined_df is the final file</span></td>
      </tr>
      <tr>
        <td id="L329" class="blob-num js-line-number" data-line-number="329"></td>
        <td id="LC329" class="blob-code blob-code-inner js-file-line">combined_df  <span class="pl-k">=</span> pcafire_nopli.append(pcafire2, <span class="pl-v">ignore_index</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L330" class="blob-num js-line-number" data-line-number="330"></td>
        <td id="LC330" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L331" class="blob-num js-line-number" data-line-number="331"></td>
        <td id="LC331" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>combined_df.to_csv(&#39;datasets/Final_Combined_Df.csv&#39;)</span></td>
      </tr>
      <tr>
        <td id="L332" class="blob-num js-line-number" data-line-number="332"></td>
        <td id="LC332" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L333" class="blob-num js-line-number" data-line-number="333"></td>
        <td id="LC333" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L334" class="blob-num js-line-number" data-line-number="334"></td>
        <td id="LC334" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L335" class="blob-num js-line-number" data-line-number="335"></td>
        <td id="LC335" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>Reading the cleaned dataset</span></td>
      </tr>
      <tr>
        <td id="L336" class="blob-num js-line-number" data-line-number="336"></td>
        <td id="LC336" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>combined_df = pd.read_csv(&#39;Final_Combined_Df.csv&#39;)</span></td>
      </tr>
      <tr>
        <td id="L337" class="blob-num js-line-number" data-line-number="337"></td>
        <td id="LC337" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L338" class="blob-num js-line-number" data-line-number="338"></td>
        <td id="LC338" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L339" class="blob-num js-line-number" data-line-number="339"></td>
        <td id="LC339" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L340" class="blob-num js-line-number" data-line-number="340"></td>
        <td id="LC340" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>Removing vacant commerical land</span></td>
      </tr>
      <tr>
        <td id="L341" class="blob-num js-line-number" data-line-number="341"></td>
        <td id="LC341" class="blob-code blob-code-inner js-file-line">combined_df <span class="pl-k">=</span> combined_df[combined_df.<span class="pl-c1">USEDESC</span><span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>VACANT COMMERCIAL LAND<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L342" class="blob-num js-line-number" data-line-number="342"></td>
        <td id="LC342" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L343" class="blob-num js-line-number" data-line-number="343"></td>
        <td id="LC343" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>converting back to 1 and 0</span></td>
      </tr>
      <tr>
        <td id="L344" class="blob-num js-line-number" data-line-number="344"></td>
        <td id="LC344" class="blob-code blob-code-inner js-file-line">combined_df[<span class="pl-s"><span class="pl-pds">&#39;</span>fire<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> combined_df[<span class="pl-s"><span class="pl-pds">&#39;</span>fire<span class="pl-pds">&#39;</span></span>].map({<span class="pl-s"><span class="pl-pds">&#39;</span>fire<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">1</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>No fire<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">0</span>})</td>
      </tr>
      <tr>
        <td id="L345" class="blob-num js-line-number" data-line-number="345"></td>
        <td id="LC345" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L346" class="blob-num js-line-number" data-line-number="346"></td>
        <td id="LC346" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>one hot encoding the features</span></td>
      </tr>
      <tr>
        <td id="L347" class="blob-num js-line-number" data-line-number="347"></td>
        <td id="LC347" class="blob-code blob-code-inner js-file-line">ohe9 <span class="pl-k">=</span> pd.get_dummies(combined_df[<span class="pl-s"><span class="pl-pds">&#39;</span>VIOLATION<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L348" class="blob-num js-line-number" data-line-number="348"></td>
        <td id="LC348" class="blob-code blob-code-inner js-file-line">ohe8 <span class="pl-k">=</span> pd.get_dummies(combined_df[<span class="pl-s"><span class="pl-pds">&#39;</span>full.code<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L349" class="blob-num js-line-number" data-line-number="349"></td>
        <td id="LC349" class="blob-code blob-code-inner js-file-line">ohe10 <span class="pl-k">=</span> pd.get_dummies(combined_df[<span class="pl-s"><span class="pl-pds">&#39;</span>INSPECTION_RESULT<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L350" class="blob-num js-line-number" data-line-number="350"></td>
        <td id="LC350" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L351" class="blob-num js-line-number" data-line-number="351"></td>
        <td id="LC351" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>concatenating the features together</span></td>
      </tr>
      <tr>
        <td id="L352" class="blob-num js-line-number" data-line-number="352"></td>
        <td id="LC352" class="blob-code blob-code-inner js-file-line">combined_df1 <span class="pl-k">=</span> pd.concat([combined_df[[<span class="pl-s"><span class="pl-pds">&#39;</span>PROPERTYADDRESS<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>PROPERTYHOUSENUM<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>CALL_CREATED_DATE<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>fire<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>fire_year<span class="pl-pds">&#39;</span></span>]],ohe8,ohe9,ohe10], <span class="pl-v">axis</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L353" class="blob-num js-line-number" data-line-number="353"></td>
        <td id="LC353" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L354" class="blob-num js-line-number" data-line-number="354"></td>
        <td id="LC354" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L355" class="blob-num js-line-number" data-line-number="355"></td>
        <td id="LC355" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>PREPARING THE TESTING DATA (final 6 months of data)</span></td>
      </tr>
      <tr>
        <td id="L356" class="blob-num js-line-number" data-line-number="356"></td>
        <td id="LC356" class="blob-code blob-code-inner js-file-line">cutoff <span class="pl-k">=</span> datetime.datetime.now() <span class="pl-k">-</span> relativedelta(<span class="pl-v">months</span><span class="pl-k">=</span><span class="pl-c1">6</span>)</td>
      </tr>
      <tr>
        <td id="L357" class="blob-num js-line-number" data-line-number="357"></td>
        <td id="LC357" class="blob-code blob-code-inner js-file-line">cutoffdate <span class="pl-k">=</span> cutoff.strftime(<span class="pl-s"><span class="pl-pds">&quot;</span>%m/<span class="pl-c1">%d</span>/%Y<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L358" class="blob-num js-line-number" data-line-number="358"></td>
        <td id="LC358" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L359" class="blob-num js-line-number" data-line-number="359"></td>
        <td id="LC359" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L360" class="blob-num js-line-number" data-line-number="360"></td>
        <td id="LC360" class="blob-code blob-code-inner js-file-line">testdata <span class="pl-k">=</span> combined_df1[combined_df1.<span class="pl-c1">CALL_CREATED_DATE</span> <span class="pl-k">&gt;</span> cutoffdate]</td>
      </tr>
      <tr>
        <td id="L361" class="blob-num js-line-number" data-line-number="361"></td>
        <td id="LC361" class="blob-code blob-code-inner js-file-line">testdata2 <span class="pl-k">=</span> testdata.groupby( [ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>CALL_CREATED_DATE<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>fire_year<span class="pl-pds">&#39;</span></span>] ).sum().reset_index()</td>
      </tr>
      <tr>
        <td id="L362" class="blob-num js-line-number" data-line-number="362"></td>
        <td id="LC362" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> testdata[<span class="pl-s"><span class="pl-pds">&#39;</span>CALL_CREATED_DATE<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L363" class="blob-num js-line-number" data-line-number="363"></td>
        <td id="LC363" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> testdata[<span class="pl-s"><span class="pl-pds">&#39;</span>fire_year<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L364" class="blob-num js-line-number" data-line-number="364"></td>
        <td id="LC364" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>testdata2 = testdata.groupby( [ &quot;PROPERTYHOUSENUM&quot;, &quot;PROPERTYADDRESS&quot;] ).sum().reset_index() #,&#39;CALL_CREATED_DATE&#39;,&#39;fire_year&#39;</span></td>
      </tr>
      <tr>
        <td id="L365" class="blob-num js-line-number" data-line-number="365"></td>
        <td id="LC365" class="blob-code blob-code-inner js-file-line">testdata2.loc[testdata2.fire <span class="pl-k">!=</span> <span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>fire<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L366" class="blob-num js-line-number" data-line-number="366"></td>
        <td id="LC366" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L367" class="blob-num js-line-number" data-line-number="367"></td>
        <td id="LC367" class="blob-code blob-code-inner js-file-line">nofire2017 <span class="pl-k">=</span> pd.concat([pcafinal[[<span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>]], testdata2[[<span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>]],testdata2[[<span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>]]]).drop_duplicates(<span class="pl-v">keep</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L368" class="blob-num js-line-number" data-line-number="368"></td>
        <td id="LC368" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L369" class="blob-num js-line-number" data-line-number="369"></td>
        <td id="LC369" class="blob-code blob-code-inner js-file-line">testdata2 <span class="pl-k">=</span> testdata2.append(nofire2017, <span class="pl-v">ignore_index</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L370" class="blob-num js-line-number" data-line-number="370"></td>
        <td id="LC370" class="blob-code blob-code-inner js-file-line">testdata2 <span class="pl-k">=</span> testdata2.fillna(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L371" class="blob-num js-line-number" data-line-number="371"></td>
        <td id="LC371" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L372" class="blob-num js-line-number" data-line-number="372"></td>
        <td id="LC372" class="blob-code blob-code-inner js-file-line">test_data <span class="pl-k">=</span> pd.merge(testdata2,pcafinal, <span class="pl-v">on</span> <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>], <span class="pl-v">how</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>left<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L373" class="blob-num js-line-number" data-line-number="373"></td>
        <td id="LC373" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>test_data.fire.value_counts()</span></td>
      </tr>
      <tr>
        <td id="L374" class="blob-num js-line-number" data-line-number="374"></td>
        <td id="LC374" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L375" class="blob-num js-line-number" data-line-number="375"></td>
        <td id="LC375" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>One hot encoding the features for the test set</span></td>
      </tr>
      <tr>
        <td id="L376" class="blob-num js-line-number" data-line-number="376"></td>
        <td id="LC376" class="blob-code blob-code-inner js-file-line">ohe1 <span class="pl-k">=</span> pd.get_dummies(test_data[<span class="pl-s"><span class="pl-pds">&#39;</span>CLASSDESC<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L377" class="blob-num js-line-number" data-line-number="377"></td>
        <td id="LC377" class="blob-code blob-code-inner js-file-line">ohe2 <span class="pl-k">=</span> pd.get_dummies(test_data[<span class="pl-s"><span class="pl-pds">&#39;</span>SCHOOLDESC<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L378" class="blob-num js-line-number" data-line-number="378"></td>
        <td id="LC378" class="blob-code blob-code-inner js-file-line">ohe3 <span class="pl-k">=</span> pd.get_dummies(test_data[<span class="pl-s"><span class="pl-pds">&#39;</span>OWNERDESC<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L379" class="blob-num js-line-number" data-line-number="379"></td>
        <td id="LC379" class="blob-code blob-code-inner js-file-line">ohe4 <span class="pl-k">=</span> pd.get_dummies(test_data[<span class="pl-s"><span class="pl-pds">&#39;</span>MUNIDESC<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L380" class="blob-num js-line-number" data-line-number="380"></td>
        <td id="LC380" class="blob-code blob-code-inner js-file-line">ohe5 <span class="pl-k">=</span> pd.get_dummies(test_data[<span class="pl-s"><span class="pl-pds">&#39;</span>NEIGHCODE<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L381" class="blob-num js-line-number" data-line-number="381"></td>
        <td id="LC381" class="blob-code blob-code-inner js-file-line">ohe6 <span class="pl-k">=</span> pd.get_dummies(test_data[<span class="pl-s"><span class="pl-pds">&#39;</span>TAXDESC<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L382" class="blob-num js-line-number" data-line-number="382"></td>
        <td id="LC382" class="blob-code blob-code-inner js-file-line">ohe7 <span class="pl-k">=</span> pd.get_dummies(test_data[<span class="pl-s"><span class="pl-pds">&#39;</span>USEDESC<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L383" class="blob-num js-line-number" data-line-number="383"></td>
        <td id="LC383" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L384" class="blob-num js-line-number" data-line-number="384"></td>
        <td id="LC384" class="blob-code blob-code-inner js-file-line">state_desc <span class="pl-k">=</span> test_data[<span class="pl-s"><span class="pl-pds">&#39;</span>CLASSDESC<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L385" class="blob-num js-line-number" data-line-number="385"></td>
        <td id="LC385" class="blob-code blob-code-inner js-file-line">school_desc<span class="pl-k">=</span> test_data[<span class="pl-s"><span class="pl-pds">&#39;</span>SCHOOLDESC<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L386" class="blob-num js-line-number" data-line-number="386"></td>
        <td id="LC386" class="blob-code blob-code-inner js-file-line">owner_desc<span class="pl-k">=</span> test_data[<span class="pl-s"><span class="pl-pds">&#39;</span>OWNERDESC<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L387" class="blob-num js-line-number" data-line-number="387"></td>
        <td id="LC387" class="blob-code blob-code-inner js-file-line">muni_desc<span class="pl-k">=</span> test_data[<span class="pl-s"><span class="pl-pds">&#39;</span>MUNIDESC<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L388" class="blob-num js-line-number" data-line-number="388"></td>
        <td id="LC388" class="blob-code blob-code-inner js-file-line">neigh_desc<span class="pl-k">=</span> test_data[<span class="pl-s"><span class="pl-pds">&#39;</span>NEIGHCODE<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L389" class="blob-num js-line-number" data-line-number="389"></td>
        <td id="LC389" class="blob-code blob-code-inner js-file-line">tax_desc<span class="pl-k">=</span> test_data[<span class="pl-s"><span class="pl-pds">&#39;</span>TAXDESC<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L390" class="blob-num js-line-number" data-line-number="390"></td>
        <td id="LC390" class="blob-code blob-code-inner js-file-line">use_desc<span class="pl-k">=</span> test_data[<span class="pl-s"><span class="pl-pds">&#39;</span>USEDESC<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L391" class="blob-num js-line-number" data-line-number="391"></td>
        <td id="LC391" class="blob-code blob-code-inner js-file-line">address<span class="pl-k">=</span> test_data[<span class="pl-s"><span class="pl-pds">&#39;</span>PROPERTYADDRESS<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L392" class="blob-num js-line-number" data-line-number="392"></td>
        <td id="LC392" class="blob-code blob-code-inner js-file-line">housenum<span class="pl-k">=</span> test_data[<span class="pl-s"><span class="pl-pds">&#39;</span>PROPERTYHOUSENUM<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L393" class="blob-num js-line-number" data-line-number="393"></td>
        <td id="LC393" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L394" class="blob-num js-line-number" data-line-number="394"></td>
        <td id="LC394" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>Deleting features not required anymore or already one hot encoded for the model</span></td>
      </tr>
      <tr>
        <td id="L395" class="blob-num js-line-number" data-line-number="395"></td>
        <td id="LC395" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> test_data[<span class="pl-s"><span class="pl-pds">&#39;</span>CALL_CREATED_DATE<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L396" class="blob-num js-line-number" data-line-number="396"></td>
        <td id="LC396" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> test_data[<span class="pl-s"><span class="pl-pds">&#39;</span>CLASSDESC<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L397" class="blob-num js-line-number" data-line-number="397"></td>
        <td id="LC397" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> test_data[<span class="pl-s"><span class="pl-pds">&#39;</span>SCHOOLDESC<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L398" class="blob-num js-line-number" data-line-number="398"></td>
        <td id="LC398" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> test_data[<span class="pl-s"><span class="pl-pds">&#39;</span>OWNERDESC<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L399" class="blob-num js-line-number" data-line-number="399"></td>
        <td id="LC399" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> test_data[<span class="pl-s"><span class="pl-pds">&#39;</span>MUNIDESC<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L400" class="blob-num js-line-number" data-line-number="400"></td>
        <td id="LC400" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> test_data[<span class="pl-s"><span class="pl-pds">&#39;</span>NEIGHCODE<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L401" class="blob-num js-line-number" data-line-number="401"></td>
        <td id="LC401" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> test_data[<span class="pl-s"><span class="pl-pds">&#39;</span>TAXDESC<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L402" class="blob-num js-line-number" data-line-number="402"></td>
        <td id="LC402" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> test_data[<span class="pl-s"><span class="pl-pds">&#39;</span>USEDESC<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L403" class="blob-num js-line-number" data-line-number="403"></td>
        <td id="LC403" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> test_data[<span class="pl-s"><span class="pl-pds">&#39;</span>fire_year<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L404" class="blob-num js-line-number" data-line-number="404"></td>
        <td id="LC404" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> test_data[<span class="pl-s"><span class="pl-pds">&#39;</span>PROPERTYADDRESS<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L405" class="blob-num js-line-number" data-line-number="405"></td>
        <td id="LC405" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> test_data[<span class="pl-s"><span class="pl-pds">&#39;</span>PROPERTYHOUSENUM<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L406" class="blob-num js-line-number" data-line-number="406"></td>
        <td id="LC406" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L407" class="blob-num js-line-number" data-line-number="407"></td>
        <td id="LC407" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>Concatenating everything back together</span></td>
      </tr>
      <tr>
        <td id="L408" class="blob-num js-line-number" data-line-number="408"></td>
        <td id="LC408" class="blob-code blob-code-inner js-file-line">encoded_testdata <span class="pl-k">=</span> pd.concat([test_data,ohe1,ohe2,ohe3,ohe4,ohe5,ohe6,ohe7], <span class="pl-v">axis</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L409" class="blob-num js-line-number" data-line-number="409"></td>
        <td id="LC409" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L410" class="blob-num js-line-number" data-line-number="410"></td>
        <td id="LC410" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>PREPARING THE TRAINING DATA</span></td>
      </tr>
      <tr>
        <td id="L411" class="blob-num js-line-number" data-line-number="411"></td>
        <td id="LC411" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L412" class="blob-num js-line-number" data-line-number="412"></td>
        <td id="LC412" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>Everything till final 6-month period is training data</span></td>
      </tr>
      <tr>
        <td id="L413" class="blob-num js-line-number" data-line-number="413"></td>
        <td id="LC413" class="blob-code blob-code-inner js-file-line">traindata1 <span class="pl-k">=</span> combined_df1[combined_df1.<span class="pl-c1">CALL_CREATED_DATE</span> <span class="pl-k">&lt;=</span> cutoffdate]</td>
      </tr>
      <tr>
        <td id="L414" class="blob-num js-line-number" data-line-number="414"></td>
        <td id="LC414" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L415" class="blob-num js-line-number" data-line-number="415"></td>
        <td id="LC415" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>Combining multiple instances of an address together</span></td>
      </tr>
      <tr>
        <td id="L416" class="blob-num js-line-number" data-line-number="416"></td>
        <td id="LC416" class="blob-code blob-code-inner js-file-line">traindata <span class="pl-k">=</span> traindata1.groupby( [ <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>CALL_CREATED_DATE<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>fire_year<span class="pl-pds">&#39;</span></span>] ).sum().reset_index()</td>
      </tr>
      <tr>
        <td id="L417" class="blob-num js-line-number" data-line-number="417"></td>
        <td id="LC417" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>Relabeling them</span></td>
      </tr>
      <tr>
        <td id="L418" class="blob-num js-line-number" data-line-number="418"></td>
        <td id="LC418" class="blob-code blob-code-inner js-file-line">traindata.loc[traindata.fire <span class="pl-k">!=</span> <span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>fire<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L419" class="blob-num js-line-number" data-line-number="419"></td>
        <td id="LC419" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L420" class="blob-num js-line-number" data-line-number="420"></td>
        <td id="LC420" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>concatenating non fire, non pca and fire instances together</span></td>
      </tr>
      <tr>
        <td id="L421" class="blob-num js-line-number" data-line-number="421"></td>
        <td id="LC421" class="blob-code blob-code-inner js-file-line">nofire_train <span class="pl-k">=</span> pd.concat([pcafinal[[<span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>]], traindata[[<span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>]],traindata[[<span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>]]]).drop_duplicates(<span class="pl-v">keep</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L422" class="blob-num js-line-number" data-line-number="422"></td>
        <td id="LC422" class="blob-code blob-code-inner js-file-line">traindata <span class="pl-k">=</span> traindata.append(nofire2017, <span class="pl-v">ignore_index</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L423" class="blob-num js-line-number" data-line-number="423"></td>
        <td id="LC423" class="blob-code blob-code-inner js-file-line">traindata <span class="pl-k">=</span> traindata.fillna(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L424" class="blob-num js-line-number" data-line-number="424"></td>
        <td id="LC424" class="blob-code blob-code-inner js-file-line">train_data <span class="pl-k">=</span> pd.merge(traindata,pcafinal, <span class="pl-v">on</span> <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYHOUSENUM<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>PROPERTYADDRESS<span class="pl-pds">&quot;</span></span>], <span class="pl-v">how</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>left<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L425" class="blob-num js-line-number" data-line-number="425"></td>
        <td id="LC425" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>train_data.fire.value_counts()</span></td>
      </tr>
      <tr>
        <td id="L426" class="blob-num js-line-number" data-line-number="426"></td>
        <td id="LC426" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L427" class="blob-num js-line-number" data-line-number="427"></td>
        <td id="LC427" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>creating on hot encoded features for the categorical values</span></td>
      </tr>
      <tr>
        <td id="L428" class="blob-num js-line-number" data-line-number="428"></td>
        <td id="LC428" class="blob-code blob-code-inner js-file-line">ohe1 <span class="pl-k">=</span> pd.get_dummies(train_data[<span class="pl-s"><span class="pl-pds">&#39;</span>CLASSDESC<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L429" class="blob-num js-line-number" data-line-number="429"></td>
        <td id="LC429" class="blob-code blob-code-inner js-file-line">ohe2 <span class="pl-k">=</span> pd.get_dummies(train_data[<span class="pl-s"><span class="pl-pds">&#39;</span>SCHOOLDESC<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L430" class="blob-num js-line-number" data-line-number="430"></td>
        <td id="LC430" class="blob-code blob-code-inner js-file-line">ohe3 <span class="pl-k">=</span> pd.get_dummies(train_data[<span class="pl-s"><span class="pl-pds">&#39;</span>OWNERDESC<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L431" class="blob-num js-line-number" data-line-number="431"></td>
        <td id="LC431" class="blob-code blob-code-inner js-file-line">ohe4 <span class="pl-k">=</span> pd.get_dummies(train_data[<span class="pl-s"><span class="pl-pds">&#39;</span>MUNIDESC<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L432" class="blob-num js-line-number" data-line-number="432"></td>
        <td id="LC432" class="blob-code blob-code-inner js-file-line">ohe5 <span class="pl-k">=</span> pd.get_dummies(train_data[<span class="pl-s"><span class="pl-pds">&#39;</span>NEIGHCODE<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L433" class="blob-num js-line-number" data-line-number="433"></td>
        <td id="LC433" class="blob-code blob-code-inner js-file-line">ohe6 <span class="pl-k">=</span> pd.get_dummies(train_data[<span class="pl-s"><span class="pl-pds">&#39;</span>TAXDESC<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L434" class="blob-num js-line-number" data-line-number="434"></td>
        <td id="LC434" class="blob-code blob-code-inner js-file-line">ohe7 <span class="pl-k">=</span> pd.get_dummies(train_data[<span class="pl-s"><span class="pl-pds">&#39;</span>USEDESC<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L435" class="blob-num js-line-number" data-line-number="435"></td>
        <td id="LC435" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L436" class="blob-num js-line-number" data-line-number="436"></td>
        <td id="LC436" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>deleting the categories</span></td>
      </tr>
      <tr>
        <td id="L437" class="blob-num js-line-number" data-line-number="437"></td>
        <td id="LC437" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> train_data[<span class="pl-s"><span class="pl-pds">&#39;</span>CLASSDESC<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L438" class="blob-num js-line-number" data-line-number="438"></td>
        <td id="LC438" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> train_data[<span class="pl-s"><span class="pl-pds">&#39;</span>CALL_CREATED_DATE<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L439" class="blob-num js-line-number" data-line-number="439"></td>
        <td id="LC439" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> train_data[<span class="pl-s"><span class="pl-pds">&#39;</span>SCHOOLDESC<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L440" class="blob-num js-line-number" data-line-number="440"></td>
        <td id="LC440" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> train_data[<span class="pl-s"><span class="pl-pds">&#39;</span>OWNERDESC<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L441" class="blob-num js-line-number" data-line-number="441"></td>
        <td id="LC441" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> train_data[<span class="pl-s"><span class="pl-pds">&#39;</span>MUNIDESC<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L442" class="blob-num js-line-number" data-line-number="442"></td>
        <td id="LC442" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> train_data[<span class="pl-s"><span class="pl-pds">&#39;</span>NEIGHCODE<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L443" class="blob-num js-line-number" data-line-number="443"></td>
        <td id="LC443" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> train_data[<span class="pl-s"><span class="pl-pds">&#39;</span>TAXDESC<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L444" class="blob-num js-line-number" data-line-number="444"></td>
        <td id="LC444" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> train_data[<span class="pl-s"><span class="pl-pds">&#39;</span>USEDESC<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L445" class="blob-num js-line-number" data-line-number="445"></td>
        <td id="LC445" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> train_data[<span class="pl-s"><span class="pl-pds">&#39;</span>fire_year<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L446" class="blob-num js-line-number" data-line-number="446"></td>
        <td id="LC446" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> train_data[<span class="pl-s"><span class="pl-pds">&#39;</span>PROPERTYADDRESS<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L447" class="blob-num js-line-number" data-line-number="447"></td>
        <td id="LC447" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> train_data[<span class="pl-s"><span class="pl-pds">&#39;</span>PROPERTYHOUSENUM<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L448" class="blob-num js-line-number" data-line-number="448"></td>
        <td id="LC448" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L449" class="blob-num js-line-number" data-line-number="449"></td>
        <td id="LC449" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>concatenating all the created features together</span></td>
      </tr>
      <tr>
        <td id="L450" class="blob-num js-line-number" data-line-number="450"></td>
        <td id="LC450" class="blob-code blob-code-inner js-file-line">encoded_traindata <span class="pl-k">=</span> pd.concat([train_data,ohe1,ohe2,ohe3,ohe4,ohe5,ohe6,ohe7], <span class="pl-v">axis</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L451" class="blob-num js-line-number" data-line-number="451"></td>
        <td id="LC451" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L452" class="blob-num js-line-number" data-line-number="452"></td>
        <td id="LC452" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>converting to array and reshaping the data to prep for model</span></td>
      </tr>
      <tr>
        <td id="L453" class="blob-num js-line-number" data-line-number="453"></td>
        <td id="LC453" class="blob-code blob-code-inner js-file-line">fireVarTrain <span class="pl-k">=</span> encoded_traindata[<span class="pl-s"><span class="pl-pds">&#39;</span>fire<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L454" class="blob-num js-line-number" data-line-number="454"></td>
        <td id="LC454" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> encoded_traindata[<span class="pl-s"><span class="pl-pds">&#39;</span>fire<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L455" class="blob-num js-line-number" data-line-number="455"></td>
        <td id="LC455" class="blob-code blob-code-inner js-file-line">X_train <span class="pl-k">=</span> np.array(encoded_traindata)</td>
      </tr>
      <tr>
        <td id="L456" class="blob-num js-line-number" data-line-number="456"></td>
        <td id="LC456" class="blob-code blob-code-inner js-file-line">y_train <span class="pl-k">=</span> np.reshape(fireVarTrain.values,[fireVarTrain.shape[<span class="pl-c1">0</span>],])</td>
      </tr>
      <tr>
        <td id="L457" class="blob-num js-line-number" data-line-number="457"></td>
        <td id="LC457" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L458" class="blob-num js-line-number" data-line-number="458"></td>
        <td id="LC458" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>converting to array and reshaping the data to prep for model</span></td>
      </tr>
      <tr>
        <td id="L459" class="blob-num js-line-number" data-line-number="459"></td>
        <td id="LC459" class="blob-code blob-code-inner js-file-line">fireVarTest <span class="pl-k">=</span> encoded_testdata[<span class="pl-s"><span class="pl-pds">&#39;</span>fire<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L460" class="blob-num js-line-number" data-line-number="460"></td>
        <td id="LC460" class="blob-code blob-code-inner js-file-line"><span class="pl-k">del</span> encoded_testdata[<span class="pl-s"><span class="pl-pds">&#39;</span>fire<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L461" class="blob-num js-line-number" data-line-number="461"></td>
        <td id="LC461" class="blob-code blob-code-inner js-file-line">X_test <span class="pl-k">=</span> np.array(encoded_testdata)</td>
      </tr>
      <tr>
        <td id="L462" class="blob-num js-line-number" data-line-number="462"></td>
        <td id="LC462" class="blob-code blob-code-inner js-file-line">y_test <span class="pl-k">=</span> np.reshape(fireVarTest.values,[fireVarTest.shape[<span class="pl-c1">0</span>],])</td>
      </tr>
      <tr>
        <td id="L463" class="blob-num js-line-number" data-line-number="463"></td>
        <td id="LC463" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L464" class="blob-num js-line-number" data-line-number="464"></td>
        <td id="LC464" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>The XG Boost model</span></td>
      </tr>
      <tr>
        <td id="L465" class="blob-num js-line-number" data-line-number="465"></td>
        <td id="LC465" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>Grid Search was taking too long a time to run hence did hyperparameter tuning manually and arrived</span></td>
      </tr>
      <tr>
        <td id="L466" class="blob-num js-line-number" data-line-number="466"></td>
        <td id="LC466" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>at the below parameters fiving the most optimal result</span></td>
      </tr>
      <tr>
        <td id="L467" class="blob-num js-line-number" data-line-number="467"></td>
        <td id="LC467" class="blob-code blob-code-inner js-file-line">model <span class="pl-k">=</span> XGBClassifier( <span class="pl-v">learning_rate</span> <span class="pl-k">=</span><span class="pl-c1">0.13</span>,</td>
      </tr>
      <tr>
        <td id="L468" class="blob-num js-line-number" data-line-number="468"></td>
        <td id="LC468" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">n_estimators</span><span class="pl-k">=</span><span class="pl-c1">1500</span>,</td>
      </tr>
      <tr>
        <td id="L469" class="blob-num js-line-number" data-line-number="469"></td>
        <td id="LC469" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">max_depth</span><span class="pl-k">=</span><span class="pl-c1">5</span>,<span class="pl-v">min_child_weight</span><span class="pl-k">=</span><span class="pl-c1">1</span>,</td>
      </tr>
      <tr>
        <td id="L470" class="blob-num js-line-number" data-line-number="470"></td>
        <td id="LC470" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">gamma</span><span class="pl-k">=</span><span class="pl-c1">0</span>,</td>
      </tr>
      <tr>
        <td id="L471" class="blob-num js-line-number" data-line-number="471"></td>
        <td id="LC471" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">subsample</span><span class="pl-k">=</span><span class="pl-c1">0.8</span>,</td>
      </tr>
      <tr>
        <td id="L472" class="blob-num js-line-number" data-line-number="472"></td>
        <td id="LC472" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">colsample_bytree</span><span class="pl-k">=</span><span class="pl-c1">0.8</span>,</td>
      </tr>
      <tr>
        <td id="L473" class="blob-num js-line-number" data-line-number="473"></td>
        <td id="LC473" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">objective</span><span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>binary:logistic<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L474" class="blob-num js-line-number" data-line-number="474"></td>
        <td id="LC474" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">nthread</span><span class="pl-k">=</span><span class="pl-c1">4</span>,</td>
      </tr>
      <tr>
        <td id="L475" class="blob-num js-line-number" data-line-number="475"></td>
        <td id="LC475" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">seed</span><span class="pl-k">=</span><span class="pl-c1">27</span>)</td>
      </tr>
      <tr>
        <td id="L476" class="blob-num js-line-number" data-line-number="476"></td>
        <td id="LC476" class="blob-code blob-code-inner js-file-line">model.fit(X_train, y_train)</td>
      </tr>
      <tr>
        <td id="L477" class="blob-num js-line-number" data-line-number="477"></td>
        <td id="LC477" class="blob-code blob-code-inner js-file-line">pred <span class="pl-k">=</span> model.predict(X_test)</td>
      </tr>
      <tr>
        <td id="L478" class="blob-num js-line-number" data-line-number="478"></td>
        <td id="LC478" class="blob-code blob-code-inner js-file-line">real <span class="pl-k">=</span> y_test</td>
      </tr>
      <tr>
        <td id="L479" class="blob-num js-line-number" data-line-number="479"></td>
        <td id="LC479" class="blob-code blob-code-inner js-file-line">cm <span class="pl-k">=</span> confusion_matrix(real, pred)</td>
      </tr>
      <tr>
        <td id="L480" class="blob-num js-line-number" data-line-number="480"></td>
        <td id="LC480" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">print</span> confusion_matrix(real, pred)</td>
      </tr>
      <tr>
        <td id="L481" class="blob-num js-line-number" data-line-number="481"></td>
        <td id="LC481" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L482" class="blob-num js-line-number" data-line-number="482"></td>
        <td id="LC482" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> sklearn.metrics <span class="pl-k">import</span> cohen_kappa_score</td>
      </tr>
      <tr>
        <td id="L483" class="blob-num js-line-number" data-line-number="483"></td>
        <td id="LC483" class="blob-code blob-code-inner js-file-line">kappa <span class="pl-k">=</span> cohen_kappa_score(real, pred)</td>
      </tr>
      <tr>
        <td id="L484" class="blob-num js-line-number" data-line-number="484"></td>
        <td id="LC484" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L485" class="blob-num js-line-number" data-line-number="485"></td>
        <td id="LC485" class="blob-code blob-code-inner js-file-line">fpr, tpr, thresholds <span class="pl-k">=</span> metrics.roc_curve(y_test, pred, <span class="pl-v">pos_label</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L486" class="blob-num js-line-number" data-line-number="486"></td>
        <td id="LC486" class="blob-code blob-code-inner js-file-line">roc_auc <span class="pl-k">=</span> metrics.auc(fpr, tpr)</td>
      </tr>
      <tr>
        <td id="L487" class="blob-num js-line-number" data-line-number="487"></td>
        <td id="LC487" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L488" class="blob-num js-line-number" data-line-number="488"></td>
        <td id="LC488" class="blob-code blob-code-inner js-file-line">acc <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Accuracy = <span class="pl-c1">{0}</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">float</span>(cm[<span class="pl-c1">0</span>][<span class="pl-c1">0</span>] <span class="pl-k">+</span> cm[<span class="pl-c1">1</span>][<span class="pl-c1">1</span>])<span class="pl-k">/</span><span class="pl-c1">len</span>(real))</td>
      </tr>
      <tr>
        <td id="L489" class="blob-num js-line-number" data-line-number="489"></td>
        <td id="LC489" class="blob-code blob-code-inner js-file-line">kapp <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>kappa score = <span class="pl-c1">{0}</span><span class="pl-pds">&#39;</span></span>.format(kappa)</td>
      </tr>
      <tr>
        <td id="L490" class="blob-num js-line-number" data-line-number="490"></td>
        <td id="LC490" class="blob-code blob-code-inner js-file-line">auc <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>AUC Score = <span class="pl-c1">{0}</span><span class="pl-pds">&#39;</span></span>.format(metrics.auc(fpr, tpr))</td>
      </tr>
      <tr>
        <td id="L491" class="blob-num js-line-number" data-line-number="491"></td>
        <td id="LC491" class="blob-code blob-code-inner js-file-line">recall <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>recall = <span class="pl-c1">{0}</span><span class="pl-pds">&#39;</span></span>.format(tpr[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L492" class="blob-num js-line-number" data-line-number="492"></td>
        <td id="LC492" class="blob-code blob-code-inner js-file-line">precis <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>precision = <span class="pl-c1">{0}</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-c1">float</span>(cm[<span class="pl-c1">1</span>][<span class="pl-c1">1</span>])<span class="pl-k">/</span>(cm[<span class="pl-c1">1</span>][<span class="pl-c1">1</span>]<span class="pl-k">+</span>cm[<span class="pl-c1">0</span>][<span class="pl-c1">1</span>]))</td>
      </tr>
      <tr>
        <td id="L493" class="blob-num js-line-number" data-line-number="493"></td>
        <td id="LC493" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L494" class="blob-num js-line-number" data-line-number="494"></td>
        <td id="LC494" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">print</span> acc</td>
      </tr>
      <tr>
        <td id="L495" class="blob-num js-line-number" data-line-number="495"></td>
        <td id="LC495" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">print</span> kapp</td>
      </tr>
      <tr>
        <td id="L496" class="blob-num js-line-number" data-line-number="496"></td>
        <td id="LC496" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">print</span> auc</td>
      </tr>
      <tr>
        <td id="L497" class="blob-num js-line-number" data-line-number="497"></td>
        <td id="LC497" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">print</span> recall</td>
      </tr>
      <tr>
        <td id="L498" class="blob-num js-line-number" data-line-number="498"></td>
        <td id="LC498" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">print</span> precis</td>
      </tr>
      <tr>
        <td id="L499" class="blob-num js-line-number" data-line-number="499"></td>
        <td id="LC499" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L500" class="blob-num js-line-number" data-line-number="500"></td>
        <td id="LC500" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L501" class="blob-num js-line-number" data-line-number="501"></td>
        <td id="LC501" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L502" class="blob-num js-line-number" data-line-number="502"></td>
        <td id="LC502" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>## Write model performance to log file:</span></td>
      </tr>
      <tr>
        <td id="L503" class="blob-num js-line-number" data-line-number="503"></td>
        <td id="LC503" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L504" class="blob-num js-line-number" data-line-number="504"></td>
        <td id="LC504" class="blob-code blob-code-inner js-file-line">log_path <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>/home/linadmin/FirePred/logs/<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L505" class="blob-num js-line-number" data-line-number="505"></td>
        <td id="LC505" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L506" class="blob-num js-line-number" data-line-number="506"></td>
        <td id="LC506" class="blob-code blob-code-inner js-file-line"><span class="pl-k">with</span> <span class="pl-c1">open</span>(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{0}</span>ModelPerformance_<span class="pl-c1">{1}</span>.txt<span class="pl-pds">&#39;</span></span>.format(log_path, datetime.datetime.now()), <span class="pl-s"><span class="pl-pds">&#39;</span>a<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> log_file:</td>
      </tr>
      <tr>
        <td id="L507" class="blob-num js-line-number" data-line-number="507"></td>
        <td id="LC507" class="blob-code blob-code-inner js-file-line">    log_file.write(cm)</td>
      </tr>
      <tr>
        <td id="L508" class="blob-num js-line-number" data-line-number="508"></td>
        <td id="LC508" class="blob-code blob-code-inner js-file-line">    log_file.write(acc)</td>
      </tr>
      <tr>
        <td id="L509" class="blob-num js-line-number" data-line-number="509"></td>
        <td id="LC509" class="blob-code blob-code-inner js-file-line">    log_file.write(kapp)</td>
      </tr>
      <tr>
        <td id="L510" class="blob-num js-line-number" data-line-number="510"></td>
        <td id="LC510" class="blob-code blob-code-inner js-file-line">    log_file.write(auc)</td>
      </tr>
      <tr>
        <td id="L511" class="blob-num js-line-number" data-line-number="511"></td>
        <td id="LC511" class="blob-code blob-code-inner js-file-line">    log_file.write(recall)</td>
      </tr>
      <tr>
        <td id="L512" class="blob-num js-line-number" data-line-number="512"></td>
        <td id="LC512" class="blob-code blob-code-inner js-file-line">    log_file.write(precis)</td>
      </tr>
      <tr>
        <td id="L513" class="blob-num js-line-number" data-line-number="513"></td>
        <td id="LC513" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L514" class="blob-num js-line-number" data-line-number="514"></td>
        <td id="LC514" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L515" class="blob-num js-line-number" data-line-number="515"></td>
        <td id="LC515" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L516" class="blob-num js-line-number" data-line-number="516"></td>
        <td id="LC516" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>Getting the probability scores</span></td>
      </tr>
      <tr>
        <td id="L517" class="blob-num js-line-number" data-line-number="517"></td>
        <td id="LC517" class="blob-code blob-code-inner js-file-line">predictions <span class="pl-k">=</span> model.predict_proba(X_test)</td>
      </tr>
      <tr>
        <td id="L518" class="blob-num js-line-number" data-line-number="518"></td>
        <td id="LC518" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">print</span> predictions</td>
      </tr>
      <tr>
        <td id="L519" class="blob-num js-line-number" data-line-number="519"></td>
        <td id="LC519" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L520" class="blob-num js-line-number" data-line-number="520"></td>
        <td id="LC520" class="blob-code blob-code-inner js-file-line">addresses <span class="pl-k">=</span> housenum <span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span><span class="pl-k">+</span> address</td>
      </tr>
      <tr>
        <td id="L521" class="blob-num js-line-number" data-line-number="521"></td>
        <td id="LC521" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L522" class="blob-num js-line-number" data-line-number="522"></td>
        <td id="LC522" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>Addresses with fire and risk score</span></td>
      </tr>
      <tr>
        <td id="L523" class="blob-num js-line-number" data-line-number="523"></td>
        <td id="LC523" class="blob-code blob-code-inner js-file-line">risk <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L524" class="blob-num js-line-number" data-line-number="524"></td>
        <td id="LC524" class="blob-code blob-code-inner js-file-line"><span class="pl-k">for</span> row <span class="pl-k">in</span> predictions:</td>
      </tr>
      <tr>
        <td id="L525" class="blob-num js-line-number" data-line-number="525"></td>
        <td id="LC525" class="blob-code blob-code-inner js-file-line">    risk.append(row[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L526" class="blob-num js-line-number" data-line-number="526"></td>
        <td id="LC526" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L527" class="blob-num js-line-number" data-line-number="527"></td>
        <td id="LC527" class="blob-code blob-code-inner js-file-line">cols <span class="pl-k">=</span> {<span class="pl-s"><span class="pl-pds">&quot;</span>Address<span class="pl-pds">&quot;</span></span>: addresses, <span class="pl-s"><span class="pl-pds">&quot;</span>Fire<span class="pl-pds">&quot;</span></span>:pred,<span class="pl-s"><span class="pl-pds">&quot;</span>RiskScore<span class="pl-pds">&quot;</span></span>:risk,<span class="pl-s"><span class="pl-pds">&quot;</span>state_desc<span class="pl-pds">&quot;</span></span>:state_desc,<span class="pl-s"><span class="pl-pds">&quot;</span>school_desc<span class="pl-pds">&quot;</span></span>:school_desc,</td>
      </tr>
      <tr>
        <td id="L528" class="blob-num js-line-number" data-line-number="528"></td>
        <td id="LC528" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;</span>owner_desc<span class="pl-pds">&quot;</span></span>:owner_desc,<span class="pl-s"><span class="pl-pds">&quot;</span>muni_desc<span class="pl-pds">&quot;</span></span>:muni_desc,<span class="pl-s"><span class="pl-pds">&quot;</span>neigh_desc<span class="pl-pds">&quot;</span></span>:neigh_desc,<span class="pl-s"><span class="pl-pds">&quot;</span>tax_desc<span class="pl-pds">&quot;</span></span>:tax_desc,<span class="pl-s"><span class="pl-pds">&quot;</span>use_desc<span class="pl-pds">&quot;</span></span>:use_desc}</td>
      </tr>
      <tr>
        <td id="L529" class="blob-num js-line-number" data-line-number="529"></td>
        <td id="LC529" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L530" class="blob-num js-line-number" data-line-number="530"></td>
        <td id="LC530" class="blob-code blob-code-inner js-file-line">Results <span class="pl-k">=</span> pd.DataFrame(cols)</td>
      </tr>
      <tr>
        <td id="L531" class="blob-num js-line-number" data-line-number="531"></td>
        <td id="LC531" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L532" class="blob-num js-line-number" data-line-number="532"></td>
        <td id="LC532" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>Writing results to the updating Results.csv</span></td>
      </tr>
      <tr>
        <td id="L533" class="blob-num js-line-number" data-line-number="533"></td>
        <td id="LC533" class="blob-code blob-code-inner js-file-line">Results.to_csv(<span class="pl-s"><span class="pl-pds">&#39;</span>/home/linadmin/FirePred/datasets/Results.csv<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L534" class="blob-num js-line-number" data-line-number="534"></td>
        <td id="LC534" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L535" class="blob-num js-line-number" data-line-number="535"></td>
        <td id="LC535" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L536" class="blob-num js-line-number" data-line-number="536"></td>
        <td id="LC536" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Writing results to a log file</span></td>
      </tr>
      <tr>
        <td id="L537" class="blob-num js-line-number" data-line-number="537"></td>
        <td id="LC537" class="blob-code blob-code-inner js-file-line">Results.to_csv(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{0}</span>Results_<span class="pl-c1">{1}</span>.csv<span class="pl-pds">&#39;</span></span>.format(log_path, datetime.datetime.now()))</td>
      </tr>
      <tr>
        <td id="L538" class="blob-num js-line-number" data-line-number="538"></td>
        <td id="LC538" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L539" class="blob-num js-line-number" data-line-number="539"></td>
        <td id="LC539" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L540" class="blob-num js-line-number" data-line-number="540"></td>
        <td id="LC540" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>Plotting the ROC curve</span></td>
      </tr>
      <tr>
        <td id="L541" class="blob-num js-line-number" data-line-number="541"></td>
        <td id="LC541" class="blob-code blob-code-inner js-file-line">plt.title(<span class="pl-s"><span class="pl-pds">&#39;</span>Receiver Operating Characteristic<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L542" class="blob-num js-line-number" data-line-number="542"></td>
        <td id="LC542" class="blob-code blob-code-inner js-file-line">plt.plot(fpr[<span class="pl-c1">1</span>:], tpr[<span class="pl-c1">1</span>:], <span class="pl-s"><span class="pl-pds">&#39;</span>b<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L543" class="blob-num js-line-number" data-line-number="543"></td>
        <td id="LC543" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>AUC = <span class="pl-c1">%0.2f</span><span class="pl-pds">&#39;</span></span><span class="pl-k">%</span> roc_auc)</td>
      </tr>
      <tr>
        <td id="L544" class="blob-num js-line-number" data-line-number="544"></td>
        <td id="LC544" class="blob-code blob-code-inner js-file-line">plt.legend(<span class="pl-v">loc</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>lower right<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L545" class="blob-num js-line-number" data-line-number="545"></td>
        <td id="LC545" class="blob-code blob-code-inner js-file-line">plt.plot([<span class="pl-c1">0</span>,<span class="pl-c1">1</span>],[<span class="pl-c1">0</span>,<span class="pl-c1">1</span>],<span class="pl-s"><span class="pl-pds">&#39;</span>r--<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L546" class="blob-num js-line-number" data-line-number="546"></td>
        <td id="LC546" class="blob-code blob-code-inner js-file-line">plt.xlim([<span class="pl-k">-</span><span class="pl-c1">0.1</span>,<span class="pl-c1">1.2</span>])</td>
      </tr>
      <tr>
        <td id="L547" class="blob-num js-line-number" data-line-number="547"></td>
        <td id="LC547" class="blob-code blob-code-inner js-file-line">plt.ylim([<span class="pl-k">-</span><span class="pl-c1">0.1</span>,<span class="pl-c1">1.2</span>])</td>
      </tr>
      <tr>
        <td id="L548" class="blob-num js-line-number" data-line-number="548"></td>
        <td id="LC548" class="blob-code blob-code-inner js-file-line">plt.ylabel(<span class="pl-s"><span class="pl-pds">&#39;</span>True Positive Rate<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L549" class="blob-num js-line-number" data-line-number="549"></td>
        <td id="LC549" class="blob-code blob-code-inner js-file-line">plt.xlabel(<span class="pl-s"><span class="pl-pds">&#39;</span>False Positive Rate<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L550" class="blob-num js-line-number" data-line-number="550"></td>
        <td id="LC550" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>plt.show()</span></td>
      </tr>
      <tr>
        <td id="L551" class="blob-num js-line-number" data-line-number="551"></td>
        <td id="LC551" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L552" class="blob-num js-line-number" data-line-number="552"></td>
        <td id="LC552" class="blob-code blob-code-inner js-file-line">png_path <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>/home/linadmin/FirePred/images/<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L553" class="blob-num js-line-number" data-line-number="553"></td>
        <td id="LC553" class="blob-code blob-code-inner js-file-line">roc_png <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">{0}</span>ROC_<span class="pl-c1">{1}</span>.png<span class="pl-pds">&quot;</span></span>.format(png_path, datetime.datetime.now())</td>
      </tr>
      <tr>
        <td id="L554" class="blob-num js-line-number" data-line-number="554"></td>
        <td id="LC554" class="blob-code blob-code-inner js-file-line">plt.savefig(roc_png, <span class="pl-v">dpi</span><span class="pl-k">=</span><span class="pl-c1">150</span>)</td>
      </tr>
      <tr>
        <td id="L555" class="blob-num js-line-number" data-line-number="555"></td>
        <td id="LC555" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L556" class="blob-num js-line-number" data-line-number="556"></td>
        <td id="LC556" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>Tree model for getting features importance</span></td>
      </tr>
      <tr>
        <td id="L557" class="blob-num js-line-number" data-line-number="557"></td>
        <td id="LC557" class="blob-code blob-code-inner js-file-line">clf <span class="pl-k">=</span> ExtraTreesClassifier()</td>
      </tr>
      <tr>
        <td id="L558" class="blob-num js-line-number" data-line-number="558"></td>
        <td id="LC558" class="blob-code blob-code-inner js-file-line">clf <span class="pl-k">=</span> clf.fit(X_train, y_train)</td>
      </tr>
      <tr>
        <td id="L559" class="blob-num js-line-number" data-line-number="559"></td>
        <td id="LC559" class="blob-code blob-code-inner js-file-line">clf.feature_importances_</td>
      </tr>
      <tr>
        <td id="L560" class="blob-num js-line-number" data-line-number="560"></td>
        <td id="LC560" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L561" class="blob-num js-line-number" data-line-number="561"></td>
        <td id="LC561" class="blob-code blob-code-inner js-file-line">UsedDf <span class="pl-k">=</span> encoded_traindata</td>
      </tr>
      <tr>
        <td id="L562" class="blob-num js-line-number" data-line-number="562"></td>
        <td id="LC562" class="blob-code blob-code-inner js-file-line">important_features <span class="pl-k">=</span> pd.Series(<span class="pl-v">data</span><span class="pl-k">=</span>clf.feature_importances_,<span class="pl-v">index</span><span class="pl-k">=</span>UsedDf.columns)</td>
      </tr>
      <tr>
        <td id="L563" class="blob-num js-line-number" data-line-number="563"></td>
        <td id="LC563" class="blob-code blob-code-inner js-file-line">important_features.sort_values(<span class="pl-v">ascending</span><span class="pl-k">=</span><span class="pl-c1">False</span>,<span class="pl-v">inplace</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L564" class="blob-num js-line-number" data-line-number="564"></td>
        <td id="LC564" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>top 20 features</span></td>
      </tr>
      <tr>
        <td id="L565" class="blob-num js-line-number" data-line-number="565"></td>
        <td id="LC565" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">print</span> important_features[<span class="pl-c1">0</span>:<span class="pl-c1">20</span>]</td>
      </tr>
      <tr>
        <td id="L566" class="blob-num js-line-number" data-line-number="566"></td>
        <td id="LC566" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L567" class="blob-num js-line-number" data-line-number="567"></td>
        <td id="LC567" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>Plotting the top 20 features</span></td>
      </tr>
      <tr>
        <td id="L568" class="blob-num js-line-number" data-line-number="568"></td>
        <td id="LC568" class="blob-code blob-code-inner js-file-line">y_pos <span class="pl-k">=</span> np.arange(<span class="pl-c1">len</span>(important_features.index[<span class="pl-c1">0</span>:<span class="pl-c1">20</span>]))</td>
      </tr>
      <tr>
        <td id="L569" class="blob-num js-line-number" data-line-number="569"></td>
        <td id="LC569" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L570" class="blob-num js-line-number" data-line-number="570"></td>
        <td id="LC570" class="blob-code blob-code-inner js-file-line">plt.bar(y_pos,important_features.values[<span class="pl-c1">0</span>:<span class="pl-c1">20</span>], <span class="pl-v">alpha</span><span class="pl-k">=</span><span class="pl-c1">0.3</span>)</td>
      </tr>
      <tr>
        <td id="L571" class="blob-num js-line-number" data-line-number="571"></td>
        <td id="LC571" class="blob-code blob-code-inner js-file-line">plt.xticks(y_pos, important_features.index[<span class="pl-c1">0</span>:<span class="pl-c1">20</span>], <span class="pl-v">rotation</span> <span class="pl-k">=</span> (<span class="pl-c1">90</span>), <span class="pl-v">fontsize</span> <span class="pl-k">=</span> <span class="pl-c1">11</span>, <span class="pl-v">ha</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>left<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L572" class="blob-num js-line-number" data-line-number="572"></td>
        <td id="LC572" class="blob-code blob-code-inner js-file-line">plt.ylabel(<span class="pl-s"><span class="pl-pds">&#39;</span>Feature Importance Scores<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L573" class="blob-num js-line-number" data-line-number="573"></td>
        <td id="LC573" class="blob-code blob-code-inner js-file-line">plt.title(<span class="pl-s"><span class="pl-pds">&#39;</span>Feature Importance<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L574" class="blob-num js-line-number" data-line-number="574"></td>
        <td id="LC574" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L575" class="blob-num js-line-number" data-line-number="575"></td>
        <td id="LC575" class="blob-code blob-code-inner js-file-line">features_png <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">{0}</span>FeatureImportance_<span class="pl-c1">{1}</span>.png<span class="pl-pds">&quot;</span></span>.format(png_path, datetime.datetime.now())</td>
      </tr>
      <tr>
        <td id="L576" class="blob-num js-line-number" data-line-number="576"></td>
        <td id="LC576" class="blob-code blob-code-inner js-file-line">plt.savefig(features_png, <span class="pl-v">dpi</span><span class="pl-k">=</span><span class="pl-c1">150</span>)</td>
      </tr>
      <tr>
        <td id="L577" class="blob-num js-line-number" data-line-number="577"></td>
        <td id="LC577" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L578" class="blob-num js-line-number" data-line-number="578"></td>
        <td id="LC578" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>plt.show()</span></td>
      </tr>
</table>

  <div class="BlobToolbar position-absolute js-file-line-actions dropdown js-menu-container js-select-menu d-none" aria-hidden="true">
    <button class="btn-octicon ml-0 px-2 p-0 bg-white border border-gray-dark rounded-1 dropdown-toggle js-menu-target" id="js-file-line-action-button" type="button" aria-expanded="false" aria-haspopup="true" aria-label="Inline file action toolbar" aria-controls="inline-file-actions">
      <svg aria-hidden="true" class="octicon octicon-kebab-horizontal" height="16" version="1.1" viewBox="0 0 13 16" width="13"><path fill-rule="evenodd" d="M1.5 9a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z"/></svg>
    </button>
    <div class="dropdown-menu-content js-menu-content" id="inline-file-actions">
      <ul class="BlobToolbar-dropdown dropdown-menu dropdown-menu-se mt-2">
        <li><a class="js-zeroclipboard dropdown-item" style="cursor:pointer;" id="js-copy-lines" data-original-text="Copy lines">Copy lines</a></li>
        <li><a class="js-zeroclipboard dropdown-item" id= "js-copy-permalink" style="cursor:pointer;" data-original-text="Copy permalink">Copy permalink</a></li>
        <li><a href="/mmadaio/temporal-fire-risk/blame/2a5756a19023aeb32c5c508403f8bbe9855a3098/riskmodel.py" class="dropdown-item js-update-url-with-hash" id="js-view-git-blame">View git blame</a></li>
          <li><a href="/mmadaio/temporal-fire-risk/issues/new" class="dropdown-item" id="js-new-issue">Open new issue</a></li>
      </ul>
    </div>
  </div>

  </div>

  </div>

  <button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="d-none">Jump to Line</button>
  <div id="jump-to-line" style="display:none">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
      <input class="form-control linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
      <button type="submit" class="btn">Go</button>
</form>  </div>


  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>

    </div>
  </div>

  </div>

      
<div class="footer container-lg px-3" role="contentinfo">
  <div class="position-relative d-flex flex-justify-between py-6 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap ">
      <li class="mr-3">&copy; 2018 <span title="0.16826s from unicorn-3432259130-0jvvt">GitHub</span>, Inc.</li>
        <li class="mr-3"><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li class="mr-3"><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li class="mr-3"><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li class="mr-3"><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>

    <a href="https://github.com" aria-label="Homepage" class="footer-octicon" title="GitHub">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewBox="0 0 16 16" width="24"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
    <ul class="list-style-none d-flex flex-wrap ">
        <li class="mr-3"><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact GitHub</a></li>
      <li class="mr-3"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li class="mr-3"><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li class="mr-3"><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
    You can't perform that action at this time.
  </div>


    
    <script crossorigin="anonymous" integrity="sha256-+xnpyXbt6GVODbcDcHIEoyLXhTRuY1OEN4fS1Kp+FA4=" src="https://assets-cdn.github.com/assets/frameworks-fb19e9c976ede8654e0db703707204a322d785346e6353843787d2d4aa7e140e.js"></script>
    
    <script async="async" crossorigin="anonymous" integrity="sha256-UYMO+8DFvDojOCewqCRx/BYHPtm4ob5q8+EqnnhQ06I=" src="https://assets-cdn.github.com/assets/github-51830efbc0c5bc3a233827b0a82471fc16073ed9b8a1be6af3e12a9e7850d3a2.js"></script>
    
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
  </div>
</div>


  </body>
</html>


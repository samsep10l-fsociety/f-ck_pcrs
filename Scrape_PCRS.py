#Designed and Engineered by samsep10l --fsociety
def get_formatted_questions():
    from bs4 import BeautifulSoup
    import re

    html_content = """

<body class="body-bg"><div class="pcrs-modal-preview" id="genericAlertModal" tabindex="-1" aria-labelledby="genericAlertModalLabel" aria-hidden="true">
    <div class="pcrs-modal-content">
        <div class="pcrs-modal-header">
            <h4 class="pcrs-modal-title" id="genericAlertModalLabel">Title</h4>
        </div>
        <div class="pcrs-modal-body"></div>
        <div class="pcrs-modal-footer"></div>
    </div>
</div>



<script src="/108_20249/static/CACHE/js/output.97694cbcc883.js"></script>




<script src="/108_20249/static/code_mirror.js"></script>

<script type="text/javascript">
    var use_simpleui = "False";
    var visualizer = null;
    var happyFaceURL = "/108_20249/static/problems/img/yellow-happy-face.png";
    var sadFaceURL = "/108_20249/static/problems/img/red-sad-face.jpg";
</script>


<script src="/108_20249/static/CACHE/js/output.e824d16dd852.js"></script>


<script id="hb_history_row" type="text/x-handlebars-template">
<div class="{{panelClass}}">
    <a data-toggle="collapse" data-parent="#history_accordian"
            style="display: block" class="pcrs-panel-heading pcrs-panel-title"
            href="#collapse_{{subPk}}">
        {{title}}
        <span class="pull-right">
            {{#if isBest}}
                <icon style="font-size:1.2em" class="star-icon"
                    title="Latest Best Submission"> </icon>
            {{/if}}
            <sup class="h_score">{{score}}</sup> /
            <sub class="h_score">{{maxScore}}</sub>
        </span>
    </a>
    <div class="pcrs-panel-collapse collapse" id="collapse_{{subPk}}">
        <div id="buttonArea"></div>
        <div id="{{mirrorId}}"></div>
        <ul class="pcrs-list-group">
        {{#each testcases}}
            <li class="testcase-{{#if passed}}success{{else}}fail{{/if}}">
                <icon class="{{#if passed}}ok{{else}}remove{{/if}}-icon"> </icon>
                {{#if visible}}
                    {{input}} -&gt; {{output}}
                {{else}}
                    {{#if description}}
                        {{description}}
                    {{else}}
                        Hidden Test
                    {{/if}}
                {{/if}}
            </li>
        {{/each}}
        </ul>
    </div>
</div>
</script>





    

<!-- requirements for pytutor.js -->

<script src="/108_20249/static/CACHE/js/output.b1d8fd323203.js"></script>

<link rel="stylesheet" href="/108_20249/static/CACHE/css/output.84ee3078216d.css" type="text/css">

<script src="/108_20249/static/CACHE/js/output.52cf61e1e74a.js"></script>

<link rel="stylesheet" href="/108_20249/static/CACHE/css/output.13231a18c7a0.css" type="text/css">



    

        <script src="/108_20249/static/csrf_protection.js" type="text/javascript"></script>
        <script src="/108_20249/static/problems/js/problems_helper.js" type="text/javascript"></script>
        <script src="/108_20249/static/problems_multiple_choice/js/mc_submit.js" type="text/javascript"></script>
        
        
        <script src="/108_20249/static/problems_short_answer/js/short_answer.js" type="text/javascript"></script>
        

        
        <script src="/108_20249/static/video_js/video.js" type="text/javascript"></script>

        <script src="/108_20249/static/content/js/video.js" type="text/javascript"></script>
        <script src="/108_20249/static/content/js/active_time.js" type="text/javascript"></script>
        <script src="/108_20249/static/bootstrap_less/bootstrap-3.2.0/js/affix.js" type="text/javascript"></script>

        <script src="/108_20249/static/content/js/events.js"></script>





        

<script src="/108_20249/static/react-0.11.1/build/react-with-addons.js"></script>
        <script src="/108_20249/static/content/build/future/components.js"></script>
        <script src="/108_20249/static/content/build/reactive_content_page.js"></script>




    <script type="text/javascript">
        $(document).keydown(function(e) {
            if (e.keyCode == 8) {
                var elID = $(document.activeElement).hasClass('textarea') || $(document.activeElement).hasClass('datetimeinput') || $(document.activeElement).hasClass('form-control');
                if (!elID) {
                    return false;
                }
            };
        });
    </script>

    <title>PCRS</title>





    
        <nav class="pcrs-navbar" role="navigation">
    <div class="pcrs-fluid">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="pcrs-navbar-header">
            <button type="button" class="pcrs-navbar-toggle" data-toggle="collapse" data-target="#student-navbar">
                <span class="at">Toggle navigation</span>
                <span class="pcrs-dropdown-icon"></span>
            </button>
            <a class="pcrs-navbar-brand" href="/108_20249/login/">PCRS</a>
        </div>
        <div class="collapse navbar-collapse" id="student-navbar">
            
                <ul class="pcrs-navbar-nav">
                    <li>
                        <a href="/108_20249/content/quests" title="Quests">
                            Quests
                        </a>
                    </li>
		</ul>
                
                <ul class="pcrs-navbar-nav">
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown">Code Editor
                            <b class="caret"></b></a>
                        <ul class="dropdown-menu">
                        
                            <li>
                                <a href="/108_20249/editor/python/submit">Python</a>
                            </li>
                        
                        
                        
                        
                        
                        
                        
                        </ul>
                    </li>
                </ul>
                
            
            <ul class="pcrs-navbar-nav-right">
                <ul class="pcrs-navbar-nav">
                    <li>
                        <a href="">Logged in as <i>yildir76</i></a>
                    </li>
                 </ul>
                

    

    <ul class="pcrs-navbar-nav">
        <li>
            <a href="/108_20249/settings">
                <i class="pcrs-settings-icon" title="Settings"></i>
            </a>
        </li>
    </ul>

    <ul class="pcrs-navbar-nav">
        <li>
            <a href="/108_20249/logout">
                <i class="pcrs-logout-icon" title="Log Out"></i>
            </a>
        </li>
    </ul>



            </ul>
        </div>
    </div>
</nav>

    


<div class="pcrs-fluid">

        
    <div id="sidebar" class="pcrs-sidebar affix-top" role="complementary" data-spy="affix" data-offset-top="60"><ul class="pcrs-sidenav" data-reactid=".n"><div class="side-bar-el" data-reactid=".n.0:$python-475"><a href="#python-475" data-reactid=".n.0:$python-475.0"><span class="problem-completed" title="7 - range #1 : completed" data-reactid=".n.0:$python-475.0.0"></span></a></div><div class="side-bar-el" data-reactid=".n.0:$python-476"><a href="#python-476" data-reactid=".n.0:$python-476.0"><span class="problem-not-attempted" title="7 - range #2: not attempted" data-reactid=".n.0:$python-476.0.0"></span></a></div><div class="side-bar-el" data-reactid=".n.0:$python-477"><a href="#python-477" data-reactid=".n.0:$python-477.0"><span class="problem-not-attempted" title="7 - range #3: not attempted" data-reactid=".n.0:$python-477.0.0"></span></a></div><div class="side-bar-el" data-reactid=".n.0:$python-478"><a href="#python-478" data-reactid=".n.0:$python-478.0"><span class="problem-not-attempted" title="7 - range #4: not attempted" data-reactid=".n.0:$python-478.0.0"></span></a></div><div class="side-bar-el" data-reactid=".n.0:$python-479"><a href="#python-479" data-reactid=".n.0:$python-479.0"><span class="problem-not-attempted" title="7 - range #5: not attempted" data-reactid=".n.0:$python-479.0.0"></span></a></div><div class="side-bar-el" data-reactid=".n.0:$python-480"><a href="#python-480" data-reactid=".n.0:$python-480.0"><span class="problem-not-attempted" title="7 - range #6: not attempted" data-reactid=".n.0:$python-480.0.0"></span></a></div><div class="side-bar-el" data-reactid=".n.0:$python-481"><a href="#python-481" data-reactid=".n.0:$python-481.0"><span class="problem-not-attempted" title="7 - range #7: not attempted" data-reactid=".n.0:$python-481.0.0"></span></a></div><div class="side-bar-el" data-reactid=".n.0:$python-482"><a href="#python-482" data-reactid=".n.0:$python-482.0"><span class="problem-not-attempted" title="7 - range #8: not attempted" data-reactid=".n.0:$python-482.0.0"></span></a></div><div class="side-bar-el" data-reactid=".n.0:$python-483"><a href="#python-483" data-reactid=".n.0:$python-483.0"><span class="problem-not-attempted" title="7 - range #9: not attempted" data-reactid=".n.0:$python-483.0.0"></span></a></div><div class="side-bar-el" data-reactid=".n.0:$python-484"><a href="#python-484" data-reactid=".n.0:$python-484.0"><span class="problem-not-attempted" title="7 - range #10: not attempted" data-reactid=".n.0:$python-484.0.0"></span></a></div><div class="side-bar-el" data-reactid=".n.0:$python-485"><a href="#python-485" data-reactid=".n.0:$python-485.0"><span class="problem-not-attempted" title="7 - range #11: not attempted" data-reactid=".n.0:$python-485.0.0"></span></a></div><div class="side-bar-el" data-reactid=".n.0:$python-486"><a href="#python-486" data-reactid=".n.0:$python-486.0"><span class="problem-not-attempted" title="7 - range #12: not attempted" data-reactid=".n.0:$python-486.0.0"></span></a></div><div class="side-bar-el" data-reactid=".n.0:$python-487"><a href="#python-487" data-reactid=".n.0:$python-487.0"><span class="problem-not-attempted" title="7 - range #13: not attempted" data-reactid=".n.0:$python-487.0.0"></span></a></div><div class="side-bar-el" data-reactid=".n.0:$python-488"><a href="#python-488" data-reactid=".n.0:$python-488.0"><span class="problem-not-attempted" title="7 - range #14: not attempted" data-reactid=".n.0:$python-488.0.0"></span></a></div><div class="side-bar-el" data-reactid=".n.0:$python-489"><a href="#python-489" data-reactid=".n.0:$python-489.0"><span class="problem-not-attempted" title="7 - range #15: not attempted" data-reactid=".n.0:$python-489.0.0"></span></a></div><div class="side-bar-el" data-reactid=".n.0:$python-490"><a href="#python-490" data-reactid=".n.0:$python-490.0"><span class="problem-completed" title="7 - range #16 : completed" data-reactid=".n.0:$python-490.0.0"></span></a></div><div class="side-bar-el" data-reactid=".n.0:$python-491"><a href="#python-491" data-reactid=".n.0:$python-491.0"><span class="problem-not-attempted" title="7 - range #17: not attempted" data-reactid=".n.0:$python-491.0.0"></span></a></div><div class="side-bar-el" data-reactid=".n.0:$python-492"><a href="#python-492" data-reactid=".n.0:$python-492.0"><span class="problem-not-attempted" title="7 - range #18: not attempted" data-reactid=".n.0:$python-492.0.0"></span></a></div><div class="side-bar-el" data-reactid=".n.0:$python-493"><a href="#python-493" data-reactid=".n.0:$python-493.0"><span class="problem-not-attempted" title="7 - range #19: not attempted" data-reactid=".n.0:$python-493.0.0"></span></a></div><div class="side-bar-el" data-reactid=".n.0:$python-494"><a href="#python-494" data-reactid=".n.0:$python-494.0"><span class="problem-not-attempted" title="7 - range #20: not attempted" data-reactid=".n.0:$python-494.0.0"></span></a></div><div class="side-bar-el" data-reactid=".n.0:$python-495"><a href="#python-495" data-reactid=".n.0:$python-495.0"><span class="problem-not-attempted" title="7 - range #21: not attempted" data-reactid=".n.0:$python-495.0.0"></span></a></div><div class="side-bar-el" data-reactid=".n.0:$python-496"><a href="#python-496" data-reactid=".n.0:$python-496.0"><span class="problem-not-attempted" title="7 - range #22: not attempted" data-reactid=".n.0:$python-496.0.0"></span></a></div><div class="side-bar-el" data-reactid=".n.0:$python-497"><a href="#python-497" data-reactid=".n.0:$python-497.0"><span class="problem-not-attempted" title="7 - range #23: not attempted" data-reactid=".n.0:$python-497.0.0"></span></a></div><div class="row" data-reactid=".n.1"><a class="side-bar-arrow" data-reactid=".n.1.0"><span class="icon-prev-inactive" data-reactid=".n.1.0.0"></span></a><a class="side-bar-arrow" data-reactid=".n.1.1"><span class="icon-next-inactive" data-reactid=".n.1.1.0"></span></a></div></ul></div>

        <div class="main-page">

                <h1>
                    
    7 - range - Part 1 of
    1

                </h1>
                 

            <hr>

                
    
                     
                

    <!--
    1. Load the YouTube API
    2. YT_Videos contain iframe information to create YT.Players
    3. YT_Players is an array of YT.Players
    (We keep these arrays because the onYouTubeIframeAPIReady
    can be called only once, so we need to store each iframe
    and create YT.Players for all of them when
    onYouTubeIframeAPIReady is invoked.)
    -->
    <script>
        var YT_Videos = new Array();
        var YT_Players = new Array();
        var tag = document.createElement('script');
        tag.src = 'https://www.youtube.com/iframe_api';
        var firstScriptTag = document.getElementsByTagName('script')[0];
        firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
    </script>


    
        
            
                
                    
                        <div id="python-475" class="code-mirror-wrapper">
                    
                    
                    
    <h3>
        
            
                <p class="widget_title">
                    7 - range #1
                </p>
            
        

        

        
            <span class="problem-score" id="score-python-475"><span title="Progress so far: complete" class="align-right" data-reactid=".0"><span class="green-checkmark-icon" data-reactid=".0.0"></span></span></span>
        

    </h3>



    <div>
        
            
                
                    <h5 class="problem-description">The `range(i, j)` function returns all numbers between `i` and `j-1`. Change the code so that it outputs the following:<br><br><br><tt>[1, 2, 3, 4]</tt><br><br>Hint: change the 4 to a 5.</h5>
                
            
        
    </div>
    <br>



    

    
        
            
            

<form method="post"> <input type="hidden" name="csrfmiddlewaretoken" value="bcQS6lRS0TePAXBSBabSwukxqoGXhs5uoFauoa1p2YQLyx5PYmZKxRDM8Xj2tbfc"> <fieldset> <ul class="nav nav-tabs tabbed-code-mirror" style="display: none;"><li class="active"><a data-toggle="tab" href="#"></a></li></ul><div class="tab-content"><div class="CodeMirror cm-s-0 cm-s- CodeMirror-wrap tab-pane active"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 8.63635px; left: 39.6591px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none; font-size: 4px;"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 29px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 29px; min-height: 53.9835px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span class="cm-builtin">p</span><span class="cm-builtin">r</span><span class="cm-builtin">i</span><span class="cm-builtin">n</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">l</span><span class="cm-builtin">i</span><span class="cm-builtin">s</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">r</span><span class="cm-builtin">a</span><span class="cm-builtin">n</span><span class="cm-builtin">g</span><span class="cm-builtin">e</span><span>(</span><span class="cm-number">1</span><span>,</span><span> </span><span class="cm-number">4</span><span>)</span><span>)</span><span>)</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div class="hash-start" style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">1</div></div><pre><span class="cm-builtin">print</span>(<span class="cm-builtin">list</span>(<span class="cm-builtin">range</span>(<span class="cm-number">1</span>, <span class="cm-number">4</span>)))</pre></div><div style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">2</div></div><pre>&nbsp;</pre></div></div><div class="CodeMirror-cursor" style="left: 10px; top: 1.98346px; height: 15.8678px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 53.9835px;"></div><div class="CodeMirror-gutters" style="left: 0.0020751px; height: 54px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 28px;"></div></div></div></div></div> </fieldset>
<div> <button class="btn reg-button" data-target="#history_window_python-475" data-toggle="modal" name="history" type="button">History</button>
<input type="submit" name="Submit" value="Submit" class="btn btn-primary green-button pull-right" id="submit-id-submit">

</div> </form>

        
    

    
        <br>
        <div class="alert-container" id="alert">
            <icon class=""></icon>
            <span></span>
            <a class="at screen-reader-text" href=""></a>
        </div>
    

    
        
<div class="pcrs-modal-history" id="history_window_python-475" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="pcrs-modal-content">
        <div class="pcrs-modal-header">
            <h4 class="pcrs-modal-title" id="myModalLabel" title="7 - range #1 History">
                
                    7 - range #1 History
                
            </h4>
                <button type="button" class="x-button-right" data-dismiss="modal" aria-hidden="false" title="Close History"></button>
        </div>
        <div class="pcrs-modal-body">
            <div class="pcrs-panel-group" id="history_accordion">

            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close
                <span class="at"> Close History </span>
            </button>
        </div>
    </div>
</div>


    

    
    <div id="grade-code" style="display: none;">
    <table id="gradeMatrix" class="pcrs-table">
        <tbody><tr class="pcrs-table-head-row">
            <td class="description">Description</td>
            <td class="expression">Test Expression</td>
            <td class="expected">Expected</td>
            <td class="result">Received</td>
            <td class="passed">Result</td>
            <!--<td class="debug">Debug</td>-->
        </tr>
    </tbody></table>
</div>

    <div class="pcrs-modal-trace" id="visualizerModal" aria-hidden="true">
    <div class="pcrs-modal-trace-content">
        <div class="pcrs-modal-body">
                <div id="visualize-code">

	            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close</button>
            <div><font size="1"><i>Visualization courtesy <a href="http://www.pythontutor.com/">Phil Guo</a></i></font></div>
        </div>

    </div>
</div>

    

<div class="pcrs-modal-trace" id="waitingModal" aria-hidden="false" style="">
  <div class="pcrs-modal-dialog">
    <div class="pcrs-modal-content" style="margin-top:20%;">
      <div class="pcrs-modal-header">
        <h4 class="pcrs-modal-title">Loading…</h4>
      </div>
      <div class="pcrs-modal-body" align="center">
        <p>Processing code, please wait…</p>
        <img src="/108_20249/static/problems/img/loading.gif" alt="Loading" height="42" width="42">
      </div>
    </div>
  </div>
</div>




    
                
            </div>
            
        
    
        
            
                
                    
                        <div id="python-476" class="code-mirror-wrapper">
                    
                    
                    
    <h3>
        
            
                <p class="widget_title">
                    7 - range #2
                </p>
            
        

        

        
            <span class="problem-score" id="score-python-476"><span title="Progress so far: not attempted" class="align-right" data-reactid=".1"><span data-reactid=".1.0"><sup data-reactid=".1.0.0">-</sup><span data-reactid=".1.0.1">/</span><sub data-reactid=".1.0.2">2</sub></span></span></span>
        

    </h3>



    <div>
        
            
                
                    <h5 class="problem-description">Change the code so that it outputs the following:<br><br><br><tt>[1, 2]</tt></h5>
                
            
        
    </div>
    <br>



    

    
        
            
            

<form method="post"> <input type="hidden" name="csrfmiddlewaretoken" value="bcQS6lRS0TePAXBSBabSwukxqoGXhs5uoFauoa1p2YQLyx5PYmZKxRDM8Xj2tbfc"> <fieldset> <ul class="nav nav-tabs tabbed-code-mirror" style="display: none;"><li class="active"><a data-toggle="tab" href="#"></a></li></ul><div class="tab-content"><div class="CodeMirror cm-s-0 cm-s- CodeMirror-wrap tab-pane active"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 8.63635px; left: 39.6591px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none; font-size: 4px;"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 29px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 29px; min-height: 53.9835px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span class="cm-builtin">p</span><span class="cm-builtin">r</span><span class="cm-builtin">i</span><span class="cm-builtin">n</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">l</span><span class="cm-builtin">i</span><span class="cm-builtin">s</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">r</span><span class="cm-builtin">a</span><span class="cm-builtin">n</span><span class="cm-builtin">g</span><span class="cm-builtin">e</span><span>(</span><span class="cm-number">1</span><span>,</span><span> </span><span class="cm-number">4</span><span>)</span><span>)</span><span>)</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div class="hash-start" style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">1</div></div><pre><span class="cm-builtin">print</span>(<span class="cm-builtin">list</span>(<span class="cm-builtin">range</span>(<span class="cm-number">1</span>, <span class="cm-number">4</span>)))</pre></div><div style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">2</div></div><pre>&nbsp;</pre></div></div><div class="CodeMirror-cursor" style="left: 10px; top: 1.98346px; height: 15.8678px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 53.9835px;"></div><div class="CodeMirror-gutters" style="left: 0.0020751px; height: 54px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 28px;"></div></div></div></div></div> </fieldset>
<div> <button class="btn reg-button" data-target="#history_window_python-476" data-toggle="modal" name="history" type="button">History</button>
<input type="submit" name="Submit" value="Submit" class="btn btn-primary green-button pull-right" id="submit-id-submit">

</div> </form>

        
    

    
        <br>
        <div class="alert-container" id="alert">
            <icon class=""></icon>
            <span></span>
            <a class="at screen-reader-text" href=""></a>
        </div>
    

    
        
<div class="pcrs-modal-history" id="history_window_python-476" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="pcrs-modal-content">
        <div class="pcrs-modal-header">
            <h4 class="pcrs-modal-title" id="myModalLabel" title="7 - range #2 History">
                
                    7 - range #2 History
                
            </h4>
                <button type="button" class="x-button-right" data-dismiss="modal" aria-hidden="false" title="Close History"></button>
        </div>
        <div class="pcrs-modal-body">
            <div class="pcrs-panel-group" id="history_accordion">

            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close
                <span class="at"> Close History </span>
            </button>
        </div>
    </div>
</div>


    

    
    <div id="grade-code" style="display: none;">
    <table id="gradeMatrix" class="pcrs-table">
        <tbody><tr class="pcrs-table-head-row">
            <td class="description">Description</td>
            <td class="expression">Test Expression</td>
            <td class="expected">Expected</td>
            <td class="result">Received</td>
            <td class="passed">Result</td>
            <!--<td class="debug">Debug</td>-->
        </tr>
    </tbody></table>
</div>

    <div class="pcrs-modal-trace" id="visualizerModal" aria-hidden="true">
    <div class="pcrs-modal-trace-content">
        <div class="pcrs-modal-body">
                <div id="visualize-code">

	            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close</button>
            <div><font size="1"><i>Visualization courtesy <a href="http://www.pythontutor.com/">Phil Guo</a></i></font></div>
        </div>

    </div>
</div>

    

<div class="pcrs-modal-trace" id="waitingModal" aria-hidden="false" style="">
  <div class="pcrs-modal-dialog">
    <div class="pcrs-modal-content" style="margin-top:20%;">
      <div class="pcrs-modal-header">
        <h4 class="pcrs-modal-title">Loading…</h4>
      </div>
      <div class="pcrs-modal-body" align="center">
        <p>Processing code, please wait…</p>
        <img src="/108_20249/static/problems/img/loading.gif" alt="Loading" height="42" width="42">
      </div>
    </div>
  </div>
</div>




    
                
            </div>
            
        
    
        
            
                
                    
                        <div id="python-477" class="code-mirror-wrapper">
                    
                    
                    
    <h3>
        
            
                <p class="widget_title">
                    7 - range #3
                </p>
            
        

        

        
            <span class="problem-score" id="score-python-477"><span title="Progress so far: not attempted" class="align-right" data-reactid=".2"><span data-reactid=".2.0"><sup data-reactid=".2.0.0">-</sup><span data-reactid=".2.0.1">/</span><sub data-reactid=".2.0.2">2</sub></span></span></span>
        

    </h3>



    <div>
        
            
                
                    <h5 class="problem-description">Change the code so that it outputs the following:<br><br><tt>[1, 2, 3, 4, 5]</tt></h5>
                
            
        
    </div>
    <br>



    

    
        
            
            

<form method="post"> <input type="hidden" name="csrfmiddlewaretoken" value="bcQS6lRS0TePAXBSBabSwukxqoGXhs5uoFauoa1p2YQLyx5PYmZKxRDM8Xj2tbfc"> <fieldset> <ul class="nav nav-tabs tabbed-code-mirror" style="display: none;"><li class="active"><a data-toggle="tab" href="#"></a></li></ul><div class="tab-content"><div class="CodeMirror cm-s-0 cm-s- CodeMirror-wrap tab-pane active"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 8.63635px; left: 39.6591px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none; font-size: 4px;"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 29px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 29px; min-height: 53.9835px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span class="cm-builtin">p</span><span class="cm-builtin">r</span><span class="cm-builtin">i</span><span class="cm-builtin">n</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">l</span><span class="cm-builtin">i</span><span class="cm-builtin">s</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">r</span><span class="cm-builtin">a</span><span class="cm-builtin">n</span><span class="cm-builtin">g</span><span class="cm-builtin">e</span><span>(</span><span class="cm-number">1</span><span>,</span><span> </span><span class="cm-number">4</span><span>)</span><span>)</span><span>)</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div class="hash-start" style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">1</div></div><pre><span class="cm-builtin">print</span>(<span class="cm-builtin">list</span>(<span class="cm-builtin">range</span>(<span class="cm-number">1</span>, <span class="cm-number">4</span>)))</pre></div><div style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">2</div></div><pre>&nbsp;</pre></div></div><div class="CodeMirror-cursor" style="left: 10px; top: 1.98346px; height: 15.8678px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 53.9835px;"></div><div class="CodeMirror-gutters" style="left: 0.0020751px; height: 54px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 28px;"></div></div></div></div></div> </fieldset>
<div> <button class="btn reg-button" data-target="#history_window_python-477" data-toggle="modal" name="history" type="button">History</button>
<input type="submit" name="Submit" value="Submit" class="btn btn-primary green-button pull-right" id="submit-id-submit">

</div> </form>

        
    

    
        <br>
        <div class="alert-container" id="alert">
            <icon class=""></icon>
            <span></span>
            <a class="at screen-reader-text" href=""></a>
        </div>
    

    
        
<div class="pcrs-modal-history" id="history_window_python-477" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="pcrs-modal-content">
        <div class="pcrs-modal-header">
            <h4 class="pcrs-modal-title" id="myModalLabel" title="7 - range #3 History">
                
                    7 - range #3 History
                
            </h4>
                <button type="button" class="x-button-right" data-dismiss="modal" aria-hidden="false" title="Close History"></button>
        </div>
        <div class="pcrs-modal-body">
            <div class="pcrs-panel-group" id="history_accordion">

            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close
                <span class="at"> Close History </span>
            </button>
        </div>
    </div>
</div>


    

    
    <div id="grade-code" style="display: none;">
    <table id="gradeMatrix" class="pcrs-table">
        <tbody><tr class="pcrs-table-head-row">
            <td class="description">Description</td>
            <td class="expression">Test Expression</td>
            <td class="expected">Expected</td>
            <td class="result">Received</td>
            <td class="passed">Result</td>
            <!--<td class="debug">Debug</td>-->
        </tr>
    </tbody></table>
</div>

    <div class="pcrs-modal-trace" id="visualizerModal" aria-hidden="true">
    <div class="pcrs-modal-trace-content">
        <div class="pcrs-modal-body">
                <div id="visualize-code">

	            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close</button>
            <div><font size="1"><i>Visualization courtesy <a href="http://www.pythontutor.com/">Phil Guo</a></i></font></div>
        </div>

    </div>
</div>

    

<div class="pcrs-modal-trace" id="waitingModal" aria-hidden="false" style="">
  <div class="pcrs-modal-dialog">
    <div class="pcrs-modal-content" style="margin-top:20%;">
      <div class="pcrs-modal-header">
        <h4 class="pcrs-modal-title">Loading…</h4>
      </div>
      <div class="pcrs-modal-body" align="center">
        <p>Processing code, please wait…</p>
        <img src="/108_20249/static/problems/img/loading.gif" alt="Loading" height="42" width="42">
      </div>
    </div>
  </div>
</div>




    
                
            </div>
            
        
    
        
            
                
                    
                        <div id="python-478" class="code-mirror-wrapper">
                    
                    
                    
    <h3>
        
            
                <p class="widget_title">
                    7 - range #4
                </p>
            
        

        

        
            <span class="problem-score" id="score-python-478"><span title="Progress so far: not attempted" class="align-right" data-reactid=".3"><span data-reactid=".3.0"><sup data-reactid=".3.0.0">-</sup><span data-reactid=".3.0.1">/</span><sub data-reactid=".3.0.2">2</sub></span></span></span>
        

    </h3>



    <div>
        
            
                
                    <h5 class="problem-description">Change the code so that it outputs the following:<br><br><tt>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]</tt></h5>
                
            
        
    </div>
    <br>



    

    
        
            
            

<form method="post"> <input type="hidden" name="csrfmiddlewaretoken" value="bcQS6lRS0TePAXBSBabSwukxqoGXhs5uoFauoa1p2YQLyx5PYmZKxRDM8Xj2tbfc"> <fieldset> <ul class="nav nav-tabs tabbed-code-mirror" style="display: none;"><li class="active"><a data-toggle="tab" href="#"></a></li></ul><div class="tab-content"><div class="CodeMirror cm-s-0 cm-s- CodeMirror-wrap tab-pane active"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 8.63647px; left: 39.6591px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none; font-size: 4px;"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 29px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 29px; min-height: 53.9835px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span class="cm-builtin">p</span><span class="cm-builtin">r</span><span class="cm-builtin">i</span><span class="cm-builtin">n</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">l</span><span class="cm-builtin">i</span><span class="cm-builtin">s</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">r</span><span class="cm-builtin">a</span><span class="cm-builtin">n</span><span class="cm-builtin">g</span><span class="cm-builtin">e</span><span>(</span><span class="cm-number">1</span><span>,</span><span> </span><span class="cm-number">4</span><span>)</span><span>)</span><span>)</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div class="hash-start" style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">1</div></div><pre><span class="cm-builtin">print</span>(<span class="cm-builtin">list</span>(<span class="cm-builtin">range</span>(<span class="cm-number">1</span>, <span class="cm-number">4</span>)))</pre></div><div style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">2</div></div><pre>&nbsp;</pre></div></div><div class="CodeMirror-cursor" style="left: 10px; top: 1.98352px; height: 15.8678px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 53.9835px;"></div><div class="CodeMirror-gutters" style="left: 0.0020751px; height: 54px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 28px;"></div></div></div></div></div> </fieldset>
<div> <button class="btn reg-button" data-target="#history_window_python-478" data-toggle="modal" name="history" type="button">History</button>
<input type="submit" name="Submit" value="Submit" class="btn btn-primary green-button pull-right" id="submit-id-submit">

</div> </form>

        
    

    
        <br>
        <div class="alert-container" id="alert">
            <icon class=""></icon>
            <span></span>
            <a class="at screen-reader-text" href=""></a>
        </div>
    

    
        
<div class="pcrs-modal-history" id="history_window_python-478" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="pcrs-modal-content">
        <div class="pcrs-modal-header">
            <h4 class="pcrs-modal-title" id="myModalLabel" title="7 - range #4 History">
                
                    7 - range #4 History
                
            </h4>
                <button type="button" class="x-button-right" data-dismiss="modal" aria-hidden="false" title="Close History"></button>
        </div>
        <div class="pcrs-modal-body">
            <div class="pcrs-panel-group" id="history_accordion">

            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close
                <span class="at"> Close History </span>
            </button>
        </div>
    </div>
</div>


    

    
    <div id="grade-code" style="display: none;">
    <table id="gradeMatrix" class="pcrs-table">
        <tbody><tr class="pcrs-table-head-row">
            <td class="description">Description</td>
            <td class="expression">Test Expression</td>
            <td class="expected">Expected</td>
            <td class="result">Received</td>
            <td class="passed">Result</td>
            <!--<td class="debug">Debug</td>-->
        </tr>
    </tbody></table>
</div>

    <div class="pcrs-modal-trace" id="visualizerModal" aria-hidden="true">
    <div class="pcrs-modal-trace-content">
        <div class="pcrs-modal-body">
                <div id="visualize-code">

	            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close</button>
            <div><font size="1"><i>Visualization courtesy <a href="http://www.pythontutor.com/">Phil Guo</a></i></font></div>
        </div>

    </div>
</div>

    

<div class="pcrs-modal-trace" id="waitingModal" aria-hidden="false" style="">
  <div class="pcrs-modal-dialog">
    <div class="pcrs-modal-content" style="margin-top:20%;">
      <div class="pcrs-modal-header">
        <h4 class="pcrs-modal-title">Loading…</h4>
      </div>
      <div class="pcrs-modal-body" align="center">
        <p>Processing code, please wait…</p>
        <img src="/108_20249/static/problems/img/loading.gif" alt="Loading" height="42" width="42">
      </div>
    </div>
  </div>
</div>




    
                
            </div>
            
        
    
        
            
                
                    
                        <div id="python-479" class="code-mirror-wrapper">
                    
                    
                    
    <h3>
        
            
                <p class="widget_title">
                    7 - range #5
                </p>
            
        

        

        
            <span class="problem-score" id="score-python-479"><span title="Progress so far: not attempted" class="align-right" data-reactid=".4"><span data-reactid=".4.0"><sup data-reactid=".4.0.0">-</sup><span data-reactid=".4.0.1">/</span><sub data-reactid=".4.0.2">2</sub></span></span></span>
        

    </h3>



    <div>
        
            
                
                    <h5 class="problem-description">Change the code so that it outputs the following:<br><br><tt>[2, 3]</tt><br><br>Hint: change the `1` to a `2`.</h5>
                
            
        
    </div>
    <br>



    

    
        
            
            

<form method="post"> <input type="hidden" name="csrfmiddlewaretoken" value="bcQS6lRS0TePAXBSBabSwukxqoGXhs5uoFauoa1p2YQLyx5PYmZKxRDM8Xj2tbfc"> <fieldset> <ul class="nav nav-tabs tabbed-code-mirror" style="display: none;"><li class="active"><a data-toggle="tab" href="#"></a></li></ul><div class="tab-content"><div class="CodeMirror cm-s-0 cm-s- CodeMirror-wrap tab-pane active"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 8.63635px; left: 39.6591px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none; font-size: 4px;"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 29px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 29px; min-height: 53.9835px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span class="cm-builtin">p</span><span class="cm-builtin">r</span><span class="cm-builtin">i</span><span class="cm-builtin">n</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">l</span><span class="cm-builtin">i</span><span class="cm-builtin">s</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">r</span><span class="cm-builtin">a</span><span class="cm-builtin">n</span><span class="cm-builtin">g</span><span class="cm-builtin">e</span><span>(</span><span class="cm-number">1</span><span>,</span><span> </span><span class="cm-number">4</span><span>)</span><span>)</span><span>)</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div class="hash-start" style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">1</div></div><pre><span class="cm-builtin">print</span>(<span class="cm-builtin">list</span>(<span class="cm-builtin">range</span>(<span class="cm-number">1</span>, <span class="cm-number">4</span>)))</pre></div><div style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">2</div></div><pre>&nbsp;</pre></div></div><div class="CodeMirror-cursor" style="left: 10px; top: 1.9834px; height: 15.8678px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 53.9835px;"></div><div class="CodeMirror-gutters" style="left: 0.0020751px; height: 54px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 28px;"></div></div></div></div></div> </fieldset>
<div> <button class="btn reg-button" data-target="#history_window_python-479" data-toggle="modal" name="history" type="button">History</button>
<input type="submit" name="Submit" value="Submit" class="btn btn-primary green-button pull-right" id="submit-id-submit">

</div> </form>

        
    

    
        <br>
        <div class="alert-container" id="alert">
            <icon class=""></icon>
            <span></span>
            <a class="at screen-reader-text" href=""></a>
        </div>
    

    
        
<div class="pcrs-modal-history" id="history_window_python-479" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="pcrs-modal-content">
        <div class="pcrs-modal-header">
            <h4 class="pcrs-modal-title" id="myModalLabel" title="7 - range #5 History">
                
                    7 - range #5 History
                
            </h4>
                <button type="button" class="x-button-right" data-dismiss="modal" aria-hidden="false" title="Close History"></button>
        </div>
        <div class="pcrs-modal-body">
            <div class="pcrs-panel-group" id="history_accordion">

            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close
                <span class="at"> Close History </span>
            </button>
        </div>
    </div>
</div>


    

    
    <div id="grade-code" style="display: none;">
    <table id="gradeMatrix" class="pcrs-table">
        <tbody><tr class="pcrs-table-head-row">
            <td class="description">Description</td>
            <td class="expression">Test Expression</td>
            <td class="expected">Expected</td>
            <td class="result">Received</td>
            <td class="passed">Result</td>
            <!--<td class="debug">Debug</td>-->
        </tr>
    </tbody></table>
</div>

    <div class="pcrs-modal-trace" id="visualizerModal" aria-hidden="true">
    <div class="pcrs-modal-trace-content">
        <div class="pcrs-modal-body">
                <div id="visualize-code">

	            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close</button>
            <div><font size="1"><i>Visualization courtesy <a href="http://www.pythontutor.com/">Phil Guo</a></i></font></div>
        </div>

    </div>
</div>

    

<div class="pcrs-modal-trace" id="waitingModal" aria-hidden="false" style="">
  <div class="pcrs-modal-dialog">
    <div class="pcrs-modal-content" style="margin-top:20%;">
      <div class="pcrs-modal-header">
        <h4 class="pcrs-modal-title">Loading…</h4>
      </div>
      <div class="pcrs-modal-body" align="center">
        <p>Processing code, please wait…</p>
        <img src="/108_20249/static/problems/img/loading.gif" alt="Loading" height="42" width="42">
      </div>
    </div>
  </div>
</div>




    
                
            </div>
            
        
    
        
            
                
                    
                        <div id="python-480" class="code-mirror-wrapper">
                    
                    
                    
    <h3>
        
            
                <p class="widget_title">
                    7 - range #6
                </p>
            
        

        

        
            <span class="problem-score" id="score-python-480"><span title="Progress so far: not attempted" class="align-right" data-reactid=".5"><span data-reactid=".5.0"><sup data-reactid=".5.0.0">-</sup><span data-reactid=".5.0.1">/</span><sub data-reactid=".5.0.2">2</sub></span></span></span>
        

    </h3>



    <div>
        
            
                
                    <h5 class="problem-description">Change the code so that it outputs the following:<br><br><tt>[2, 3, 4, 5, 6, 7]</tt></h5>
                
            
        
    </div>
    <br>



    

    
        
            
            

<form method="post"> <input type="hidden" name="csrfmiddlewaretoken" value="bcQS6lRS0TePAXBSBabSwukxqoGXhs5uoFauoa1p2YQLyx5PYmZKxRDM8Xj2tbfc"> <fieldset> <ul class="nav nav-tabs tabbed-code-mirror" style="display: none;"><li class="active"><a data-toggle="tab" href="#"></a></li></ul><div class="tab-content"><div class="CodeMirror cm-s-0 cm-s- CodeMirror-wrap tab-pane active"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 8.63635px; left: 39.6591px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none; font-size: 4px;"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 29px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 29px; min-height: 53.9835px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span class="cm-builtin">p</span><span class="cm-builtin">r</span><span class="cm-builtin">i</span><span class="cm-builtin">n</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">l</span><span class="cm-builtin">i</span><span class="cm-builtin">s</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">r</span><span class="cm-builtin">a</span><span class="cm-builtin">n</span><span class="cm-builtin">g</span><span class="cm-builtin">e</span><span>(</span><span class="cm-number">1</span><span>,</span><span> </span><span class="cm-number">8</span><span>)</span><span>)</span><span>)</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div class="hash-start" style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">1</div></div><pre><span class="cm-builtin">print</span>(<span class="cm-builtin">list</span>(<span class="cm-builtin">range</span>(<span class="cm-number">1</span>, <span class="cm-number">8</span>)))</pre></div><div style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">2</div></div><pre>&nbsp;</pre></div></div><div class="CodeMirror-cursor" style="left: 10px; top: 1.98352px; height: 15.8678px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 53.9835px;"></div><div class="CodeMirror-gutters" style="left: 0.0020751px; height: 54px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 28px;"></div></div></div></div></div> </fieldset>
<div> <button class="btn reg-button" data-target="#history_window_python-480" data-toggle="modal" name="history" type="button">History</button>
<input type="submit" name="Submit" value="Submit" class="btn btn-primary green-button pull-right" id="submit-id-submit">

</div> </form>

        
    

    
        <br>
        <div class="alert-container" id="alert">
            <icon class=""></icon>
            <span></span>
            <a class="at screen-reader-text" href=""></a>
        </div>
    

    
        
<div class="pcrs-modal-history" id="history_window_python-480" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="pcrs-modal-content">
        <div class="pcrs-modal-header">
            <h4 class="pcrs-modal-title" id="myModalLabel" title="7 - range #6 History">
                
                    7 - range #6 History
                
            </h4>
                <button type="button" class="x-button-right" data-dismiss="modal" aria-hidden="false" title="Close History"></button>
        </div>
        <div class="pcrs-modal-body">
            <div class="pcrs-panel-group" id="history_accordion">

            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close
                <span class="at"> Close History </span>
            </button>
        </div>
    </div>
</div>


    

    
    <div id="grade-code" style="display: none;">
    <table id="gradeMatrix" class="pcrs-table">
        <tbody><tr class="pcrs-table-head-row">
            <td class="description">Description</td>
            <td class="expression">Test Expression</td>
            <td class="expected">Expected</td>
            <td class="result">Received</td>
            <td class="passed">Result</td>
            <!--<td class="debug">Debug</td>-->
        </tr>
    </tbody></table>
</div>

    <div class="pcrs-modal-trace" id="visualizerModal" aria-hidden="true">
    <div class="pcrs-modal-trace-content">
        <div class="pcrs-modal-body">
                <div id="visualize-code">

	            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close</button>
            <div><font size="1"><i>Visualization courtesy <a href="http://www.pythontutor.com/">Phil Guo</a></i></font></div>
        </div>

    </div>
</div>

    

<div class="pcrs-modal-trace" id="waitingModal" aria-hidden="false" style="">
  <div class="pcrs-modal-dialog">
    <div class="pcrs-modal-content" style="margin-top:20%;">
      <div class="pcrs-modal-header">
        <h4 class="pcrs-modal-title">Loading…</h4>
      </div>
      <div class="pcrs-modal-body" align="center">
        <p>Processing code, please wait…</p>
        <img src="/108_20249/static/problems/img/loading.gif" alt="Loading" height="42" width="42">
      </div>
    </div>
  </div>
</div>




    
                
            </div>
            
        
    
        
            
                
                    
                        <div id="python-481" class="code-mirror-wrapper">
                    
                    
                    
    <h3>
        
            
                <p class="widget_title">
                    7 - range #7
                </p>
            
        

        

        
            <span class="problem-score" id="score-python-481"><span title="Progress so far: not attempted" class="align-right" data-reactid=".6"><span data-reactid=".6.0"><sup data-reactid=".6.0.0">-</sup><span data-reactid=".6.0.1">/</span><sub data-reactid=".6.0.2">2</sub></span></span></span>
        

    </h3>



    <div>
        
            
                
                    <h5 class="problem-description">Change the code so that it outputs the following:<br><br><tt>[4, 5, 6, 7]</tt><br><br>Hint: you will need to change both arguments to the `range()` function.</h5>
                
            
        
    </div>
    <br>



    

    
        
            
            

<form method="post"> <input type="hidden" name="csrfmiddlewaretoken" value="bcQS6lRS0TePAXBSBabSwukxqoGXhs5uoFauoa1p2YQLyx5PYmZKxRDM8Xj2tbfc"> <fieldset> <ul class="nav nav-tabs tabbed-code-mirror" style="display: none;"><li class="active"><a data-toggle="tab" href="#"></a></li></ul><div class="tab-content"><div class="CodeMirror cm-s-0 cm-s- CodeMirror-wrap tab-pane active"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 8.63635px; left: 39.6591px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none; font-size: 4px;"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 29px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 29px; min-height: 53.9835px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span class="cm-builtin">p</span><span class="cm-builtin">r</span><span class="cm-builtin">i</span><span class="cm-builtin">n</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">l</span><span class="cm-builtin">i</span><span class="cm-builtin">s</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">r</span><span class="cm-builtin">a</span><span class="cm-builtin">n</span><span class="cm-builtin">g</span><span class="cm-builtin">e</span><span>(</span><span class="cm-number">1</span><span>,</span><span> </span><span class="cm-number">9</span><span>)</span><span>)</span><span>)</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div class="hash-start" style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">1</div></div><pre><span class="cm-builtin">print</span>(<span class="cm-builtin">list</span>(<span class="cm-builtin">range</span>(<span class="cm-number">1</span>, <span class="cm-number">9</span>)))</pre></div><div style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">2</div></div><pre>&nbsp;</pre></div></div><div class="CodeMirror-cursor" style="left: 10px; top: 1.98352px; height: 15.8678px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 53.9835px;"></div><div class="CodeMirror-gutters" style="left: 0.0020751px; height: 54px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 28px;"></div></div></div></div></div> </fieldset>
<div> <button class="btn reg-button" data-target="#history_window_python-481" data-toggle="modal" name="history" type="button">History</button>
<input type="submit" name="Submit" value="Submit" class="btn btn-primary green-button pull-right" id="submit-id-submit">

</div> </form>

        
    

    
        <br>
        <div class="alert-container" id="alert">
            <icon class=""></icon>
            <span></span>
            <a class="at screen-reader-text" href=""></a>
        </div>
    

    
        
<div class="pcrs-modal-history" id="history_window_python-481" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="pcrs-modal-content">
        <div class="pcrs-modal-header">
            <h4 class="pcrs-modal-title" id="myModalLabel" title="7 - range #7 History">
                
                    7 - range #7 History
                
            </h4>
                <button type="button" class="x-button-right" data-dismiss="modal" aria-hidden="false" title="Close History"></button>
        </div>
        <div class="pcrs-modal-body">
            <div class="pcrs-panel-group" id="history_accordion">

            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close
                <span class="at"> Close History </span>
            </button>
        </div>
    </div>
</div>


    

    
    <div id="grade-code" style="display: none;">
    <table id="gradeMatrix" class="pcrs-table">
        <tbody><tr class="pcrs-table-head-row">
            <td class="description">Description</td>
            <td class="expression">Test Expression</td>
            <td class="expected">Expected</td>
            <td class="result">Received</td>
            <td class="passed">Result</td>
            <!--<td class="debug">Debug</td>-->
        </tr>
    </tbody></table>
</div>

    <div class="pcrs-modal-trace" id="visualizerModal" aria-hidden="true">
    <div class="pcrs-modal-trace-content">
        <div class="pcrs-modal-body">
                <div id="visualize-code">

	            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close</button>
            <div><font size="1"><i>Visualization courtesy <a href="http://www.pythontutor.com/">Phil Guo</a></i></font></div>
        </div>

    </div>
</div>

    

<div class="pcrs-modal-trace" id="waitingModal" aria-hidden="false" style="">
  <div class="pcrs-modal-dialog">
    <div class="pcrs-modal-content" style="margin-top:20%;">
      <div class="pcrs-modal-header">
        <h4 class="pcrs-modal-title">Loading…</h4>
      </div>
      <div class="pcrs-modal-body" align="center">
        <p>Processing code, please wait…</p>
        <img src="/108_20249/static/problems/img/loading.gif" alt="Loading" height="42" width="42">
      </div>
    </div>
  </div>
</div>




    
                
            </div>
            
        
    
        
            
                
                    
                        <div id="python-482" class="code-mirror-wrapper">
                    
                    
                    
    <h3>
        
            
                <p class="widget_title">
                    7 - range #8
                </p>
            
        

        

        
            <span class="problem-score" id="score-python-482"><span title="Progress so far: not attempted" class="align-right" data-reactid=".7"><span data-reactid=".7.0"><sup data-reactid=".7.0.0">-</sup><span data-reactid=".7.0.1">/</span><sub data-reactid=".7.0.2">2</sub></span></span></span>
        

    </h3>



    <div>
        
            
                
                    <h5 class="problem-description">Change the code so that it outputs the following:<br><br><tt>[218, 219, 220, 221, 222]</tt></h5>
                
            
        
    </div>
    <br>



    

    
        
            
            

<form method="post"> <input type="hidden" name="csrfmiddlewaretoken" value="bcQS6lRS0TePAXBSBabSwukxqoGXhs5uoFauoa1p2YQLyx5PYmZKxRDM8Xj2tbfc"> <fieldset> <ul class="nav nav-tabs tabbed-code-mirror" style="display: none;"><li class="active"><a data-toggle="tab" href="#"></a></li></ul><div class="tab-content"><div class="CodeMirror cm-s-0 cm-s- CodeMirror-wrap tab-pane active"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 8.63647px; left: 39.6591px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none; font-size: 4px;"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 29px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 29px; min-height: 53.9835px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span class="cm-builtin">p</span><span class="cm-builtin">r</span><span class="cm-builtin">i</span><span class="cm-builtin">n</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">l</span><span class="cm-builtin">i</span><span class="cm-builtin">s</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">r</span><span class="cm-builtin">a</span><span class="cm-builtin">n</span><span class="cm-builtin">g</span><span class="cm-builtin">e</span><span>(</span><span class="cm-number">1</span><span>,</span><span> </span><span class="cm-number">9</span><span>)</span><span>)</span><span>)</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div class="hash-start" style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">1</div></div><pre><span class="cm-builtin">print</span>(<span class="cm-builtin">list</span>(<span class="cm-builtin">range</span>(<span class="cm-number">1</span>, <span class="cm-number">9</span>)))</pre></div><div style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">2</div></div><pre>&nbsp;</pre></div></div><div class="CodeMirror-cursor" style="left: 10px; top: 1.98364px; height: 15.8678px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 53.9835px;"></div><div class="CodeMirror-gutters" style="left: 0.0020751px; height: 54px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 28px;"></div></div></div></div></div> </fieldset>
<div> <button class="btn reg-button" data-target="#history_window_python-482" data-toggle="modal" name="history" type="button">History</button>
<input type="submit" name="Submit" value="Submit" class="btn btn-primary green-button pull-right" id="submit-id-submit">

</div> </form>

        
    

    
        <br>
        <div class="alert-container" id="alert">
            <icon class=""></icon>
            <span></span>
            <a class="at screen-reader-text" href=""></a>
        </div>
    

    
        
<div class="pcrs-modal-history" id="history_window_python-482" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="pcrs-modal-content">
        <div class="pcrs-modal-header">
            <h4 class="pcrs-modal-title" id="myModalLabel" title="7 - range #8 History">
                
                    7 - range #8 History
                
            </h4>
                <button type="button" class="x-button-right" data-dismiss="modal" aria-hidden="false" title="Close History"></button>
        </div>
        <div class="pcrs-modal-body">
            <div class="pcrs-panel-group" id="history_accordion">

            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close
                <span class="at"> Close History </span>
            </button>
        </div>
    </div>
</div>


    

    
    <div id="grade-code" style="display: none;">
    <table id="gradeMatrix" class="pcrs-table">
        <tbody><tr class="pcrs-table-head-row">
            <td class="description">Description</td>
            <td class="expression">Test Expression</td>
            <td class="expected">Expected</td>
            <td class="result">Received</td>
            <td class="passed">Result</td>
            <!--<td class="debug">Debug</td>-->
        </tr>
    </tbody></table>
</div>

    <div class="pcrs-modal-trace" id="visualizerModal" aria-hidden="true">
    <div class="pcrs-modal-trace-content">
        <div class="pcrs-modal-body">
                <div id="visualize-code">

	            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close</button>
            <div><font size="1"><i>Visualization courtesy <a href="http://www.pythontutor.com/">Phil Guo</a></i></font></div>
        </div>

    </div>
</div>

    

<div class="pcrs-modal-trace" id="waitingModal" aria-hidden="false" style="">
  <div class="pcrs-modal-dialog">
    <div class="pcrs-modal-content" style="margin-top:20%;">
      <div class="pcrs-modal-header">
        <h4 class="pcrs-modal-title">Loading…</h4>
      </div>
      <div class="pcrs-modal-body" align="center">
        <p>Processing code, please wait…</p>
        <img src="/108_20249/static/problems/img/loading.gif" alt="Loading" height="42" width="42">
      </div>
    </div>
  </div>
</div>




    
                
            </div>
            
        
    
        
            
                
                    
                        <div id="python-483" class="code-mirror-wrapper">
                    
                    
                    
    <h3>
        
            
                <p class="widget_title">
                    7 - range #9
                </p>
            
        

        

        
            <span class="problem-score" id="score-python-483"><span title="Progress so far: not attempted" class="align-right" data-reactid=".8"><span data-reactid=".8.0"><sup data-reactid=".8.0.0">-</sup><span data-reactid=".8.0.1">/</span><sub data-reactid=".8.0.2">2</sub></span></span></span>
        

    </h3>



    <div>
        
            
                
                    <h5 class="problem-description">Change the code so that it outputs the following:<br><br><tt>[-5, -4, -3, -2]</tt><br><br>Hint: both arguments to the `range()` function will be negative.</h5>
                
            
        
    </div>
    <br>



    

    
        
            
            

<form method="post"> <input type="hidden" name="csrfmiddlewaretoken" value="bcQS6lRS0TePAXBSBabSwukxqoGXhs5uoFauoa1p2YQLyx5PYmZKxRDM8Xj2tbfc"> <fieldset> <ul class="nav nav-tabs tabbed-code-mirror" style="display: none;"><li class="active"><a data-toggle="tab" href="#"></a></li></ul><div class="tab-content"><div class="CodeMirror cm-s-0 cm-s- CodeMirror-wrap tab-pane active"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 8.63647px; left: 39.6591px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none; font-size: 4px;"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 29px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 29px; min-height: 53.9835px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span class="cm-builtin">p</span><span class="cm-builtin">r</span><span class="cm-builtin">i</span><span class="cm-builtin">n</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">l</span><span class="cm-builtin">i</span><span class="cm-builtin">s</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">r</span><span class="cm-builtin">a</span><span class="cm-builtin">n</span><span class="cm-builtin">g</span><span class="cm-builtin">e</span><span>(</span><span class="cm-number">1</span><span>,</span><span> </span><span class="cm-number">9</span><span>)</span><span>)</span><span>)</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div class="hash-start" style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">1</div></div><pre><span class="cm-builtin">print</span>(<span class="cm-builtin">list</span>(<span class="cm-builtin">range</span>(<span class="cm-number">1</span>, <span class="cm-number">9</span>)))</pre></div><div style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">2</div></div><pre>&nbsp;</pre></div></div><div class="CodeMirror-cursor" style="left: 10px; top: 1.98364px; height: 15.8678px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 53.9835px;"></div><div class="CodeMirror-gutters" style="left: 0.0020751px; height: 54px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 28px;"></div></div></div></div></div> </fieldset>
<div> <button class="btn reg-button" data-target="#history_window_python-483" data-toggle="modal" name="history" type="button">History</button>
<input type="submit" name="Submit" value="Submit" class="btn btn-primary green-button pull-right" id="submit-id-submit">

</div> </form>

        
    

    
        <br>
        <div class="alert-container" id="alert">
            <icon class=""></icon>
            <span></span>
            <a class="at screen-reader-text" href=""></a>
        </div>
    

    
        
<div class="pcrs-modal-history" id="history_window_python-483" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="pcrs-modal-content">
        <div class="pcrs-modal-header">
            <h4 class="pcrs-modal-title" id="myModalLabel" title="7 - range #9 History">
                
                    7 - range #9 History
                
            </h4>
                <button type="button" class="x-button-right" data-dismiss="modal" aria-hidden="false" title="Close History"></button>
        </div>
        <div class="pcrs-modal-body">
            <div class="pcrs-panel-group" id="history_accordion">

            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close
                <span class="at"> Close History </span>
            </button>
        </div>
    </div>
</div>


    

    
    <div id="grade-code" style="display: none;">
    <table id="gradeMatrix" class="pcrs-table">
        <tbody><tr class="pcrs-table-head-row">
            <td class="description">Description</td>
            <td class="expression">Test Expression</td>
            <td class="expected">Expected</td>
            <td class="result">Received</td>
            <td class="passed">Result</td>
            <!--<td class="debug">Debug</td>-->
        </tr>
    </tbody></table>
</div>

    <div class="pcrs-modal-trace" id="visualizerModal" aria-hidden="true">
    <div class="pcrs-modal-trace-content">
        <div class="pcrs-modal-body">
                <div id="visualize-code">

	            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close</button>
            <div><font size="1"><i>Visualization courtesy <a href="http://www.pythontutor.com/">Phil Guo</a></i></font></div>
        </div>

    </div>
</div>

    

<div class="pcrs-modal-trace" id="waitingModal" aria-hidden="false" style="">
  <div class="pcrs-modal-dialog">
    <div class="pcrs-modal-content" style="margin-top:20%;">
      <div class="pcrs-modal-header">
        <h4 class="pcrs-modal-title">Loading…</h4>
      </div>
      <div class="pcrs-modal-body" align="center">
        <p>Processing code, please wait…</p>
        <img src="/108_20249/static/problems/img/loading.gif" alt="Loading" height="42" width="42">
      </div>
    </div>
  </div>
</div>




    
                
            </div>
            
        
    
        
            
                
                    
                        <div id="python-484" class="code-mirror-wrapper">
                    
                    
                    
    <h3>
        
            
                <p class="widget_title">
                    7 - range #10
                </p>
            
        

        

        
            <span class="problem-score" id="score-python-484"><span title="Progress so far: not attempted" class="align-right" data-reactid=".9"><span data-reactid=".9.0"><sup data-reactid=".9.0.0">-</sup><span data-reactid=".9.0.1">/</span><sub data-reactid=".9.0.2">2</sub></span></span></span>
        

    </h3>



    <div>
        
            
                
                    <h5 class="problem-description">Change the code so that it outputs the following:<br><br><tt>[-3, -2, -1, 0, 1, 2]</tt><br><br>Hint: the first argument to the `range()` function will be negative.</h5>
                
            
        
    </div>
    <br>



    

    
        
            
            

<form method="post"> <input type="hidden" name="csrfmiddlewaretoken" value="bcQS6lRS0TePAXBSBabSwukxqoGXhs5uoFauoa1p2YQLyx5PYmZKxRDM8Xj2tbfc"> <fieldset> <ul class="nav nav-tabs tabbed-code-mirror" style="display: none;"><li class="active"><a data-toggle="tab" href="#"></a></li></ul><div class="tab-content"><div class="CodeMirror cm-s-0 cm-s- CodeMirror-wrap tab-pane active"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 8.63623px; left: 39.6591px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none; font-size: 4px;"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 29px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 29px; min-height: 53.9835px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span class="cm-builtin">p</span><span class="cm-builtin">r</span><span class="cm-builtin">i</span><span class="cm-builtin">n</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">l</span><span class="cm-builtin">i</span><span class="cm-builtin">s</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">r</span><span class="cm-builtin">a</span><span class="cm-builtin">n</span><span class="cm-builtin">g</span><span class="cm-builtin">e</span><span>(</span><span class="cm-number">1</span><span>,</span><span> </span><span class="cm-number">9</span><span>)</span><span>)</span><span>)</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div class="hash-start" style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">1</div></div><pre><span class="cm-builtin">print</span>(<span class="cm-builtin">list</span>(<span class="cm-builtin">range</span>(<span class="cm-number">1</span>, <span class="cm-number">9</span>)))</pre></div><div style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">2</div></div><pre>&nbsp;</pre></div></div><div class="CodeMirror-cursor" style="left: 10px; top: 1.9834px; height: 15.8678px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 53.9835px;"></div><div class="CodeMirror-gutters" style="left: 0.0020751px; height: 54px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 28px;"></div></div></div></div></div> </fieldset>
<div> <button class="btn reg-button" data-target="#history_window_python-484" data-toggle="modal" name="history" type="button">History</button>
<input type="submit" name="Submit" value="Submit" class="btn btn-primary green-button pull-right" id="submit-id-submit">

</div> </form>

        
    

    
        <br>
        <div class="alert-container" id="alert">
            <icon class=""></icon>
            <span></span>
            <a class="at screen-reader-text" href=""></a>
        </div>
    

    
        
<div class="pcrs-modal-history" id="history_window_python-484" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="pcrs-modal-content">
        <div class="pcrs-modal-header">
            <h4 class="pcrs-modal-title" id="myModalLabel" title="7 - range #10 History">
                
                    7 - range #10 History
                
            </h4>
                <button type="button" class="x-button-right" data-dismiss="modal" aria-hidden="false" title="Close History"></button>
        </div>
        <div class="pcrs-modal-body">
            <div class="pcrs-panel-group" id="history_accordion">

            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close
                <span class="at"> Close History </span>
            </button>
        </div>
    </div>
</div>


    

    
    <div id="grade-code" style="display: none;">
    <table id="gradeMatrix" class="pcrs-table">
        <tbody><tr class="pcrs-table-head-row">
            <td class="description">Description</td>
            <td class="expression">Test Expression</td>
            <td class="expected">Expected</td>
            <td class="result">Received</td>
            <td class="passed">Result</td>
            <!--<td class="debug">Debug</td>-->
        </tr>
    </tbody></table>
</div>

    <div class="pcrs-modal-trace" id="visualizerModal" aria-hidden="true">
    <div class="pcrs-modal-trace-content">
        <div class="pcrs-modal-body">
                <div id="visualize-code">

	            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close</button>
            <div><font size="1"><i>Visualization courtesy <a href="http://www.pythontutor.com/">Phil Guo</a></i></font></div>
        </div>

    </div>
</div>

    

<div class="pcrs-modal-trace" id="waitingModal" aria-hidden="false" style="">
  <div class="pcrs-modal-dialog">
    <div class="pcrs-modal-content" style="margin-top:20%;">
      <div class="pcrs-modal-header">
        <h4 class="pcrs-modal-title">Loading…</h4>
      </div>
      <div class="pcrs-modal-body" align="center">
        <p>Processing code, please wait…</p>
        <img src="/108_20249/static/problems/img/loading.gif" alt="Loading" height="42" width="42">
      </div>
    </div>
  </div>
</div>




    
                
            </div>
            
        
    
        
            
                
                    
                        <div id="python-485" class="code-mirror-wrapper">
                    
                    
                    
    <h3>
        
            
                <p class="widget_title">
                    7 - range #11
                </p>
            
        

        

        
            <span class="problem-score" id="score-python-485"><span title="Progress so far: not attempted" class="align-right" data-reactid=".a"><span data-reactid=".a.0"><sup data-reactid=".a.0.0">-</sup><span data-reactid=".a.0.1">/</span><sub data-reactid=".a.0.2">2</sub></span></span></span>
        

    </h3>



    <div>
        
            
                
                    <h5 class="problem-description">Change the code so that it outputs from `-18` to `173`, inclusive. So the output will be:<br><br><tt>[-18, -17, -16,..., 171, 172, 173]</tt></h5>
                
            
        
    </div>
    <br>



    

    
        
            
            

<form method="post"> <input type="hidden" name="csrfmiddlewaretoken" value="bcQS6lRS0TePAXBSBabSwukxqoGXhs5uoFauoa1p2YQLyx5PYmZKxRDM8Xj2tbfc"> <fieldset> <ul class="nav nav-tabs tabbed-code-mirror" style="display: none;"><li class="active"><a data-toggle="tab" href="#"></a></li></ul><div class="tab-content"><div class="CodeMirror cm-s-0 cm-s- CodeMirror-wrap tab-pane active"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 8.63623px; left: 39.6591px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none; font-size: 4px;"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 29px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 29px; min-height: 53.9835px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span class="cm-builtin">p</span><span class="cm-builtin">r</span><span class="cm-builtin">i</span><span class="cm-builtin">n</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">l</span><span class="cm-builtin">i</span><span class="cm-builtin">s</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">r</span><span class="cm-builtin">a</span><span class="cm-builtin">n</span><span class="cm-builtin">g</span><span class="cm-builtin">e</span><span>(</span><span class="cm-number">1</span><span>,</span><span> </span><span class="cm-number">9</span><span>)</span><span>)</span><span>)</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div class="hash-start" style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">1</div></div><pre><span class="cm-builtin">print</span>(<span class="cm-builtin">list</span>(<span class="cm-builtin">range</span>(<span class="cm-number">1</span>, <span class="cm-number">9</span>)))</pre></div><div style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">2</div></div><pre>&nbsp;</pre></div></div><div class="CodeMirror-cursor" style="left: 10px; top: 1.9834px; height: 15.8678px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 53.9835px;"></div><div class="CodeMirror-gutters" style="left: 0.0020751px; height: 54px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 28px;"></div></div></div></div></div> </fieldset>
<div> <button class="btn reg-button" data-target="#history_window_python-485" data-toggle="modal" name="history" type="button">History</button>
<input type="submit" name="Submit" value="Submit" class="btn btn-primary green-button pull-right" id="submit-id-submit">

</div> </form>

        
    

    
        <br>
        <div class="alert-container" id="alert">
            <icon class=""></icon>
            <span></span>
            <a class="at screen-reader-text" href=""></a>
        </div>
    

    
        
<div class="pcrs-modal-history" id="history_window_python-485" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="pcrs-modal-content">
        <div class="pcrs-modal-header">
            <h4 class="pcrs-modal-title" id="myModalLabel" title="7 - range #11 History">
                
                    7 - range #11 History
                
            </h4>
                <button type="button" class="x-button-right" data-dismiss="modal" aria-hidden="false" title="Close History"></button>
        </div>
        <div class="pcrs-modal-body">
            <div class="pcrs-panel-group" id="history_accordion">

            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close
                <span class="at"> Close History </span>
            </button>
        </div>
    </div>
</div>


    

    
    <div id="grade-code" style="display: none;">
    <table id="gradeMatrix" class="pcrs-table">
        <tbody><tr class="pcrs-table-head-row">
            <td class="description">Description</td>
            <td class="expression">Test Expression</td>
            <td class="expected">Expected</td>
            <td class="result">Received</td>
            <td class="passed">Result</td>
            <!--<td class="debug">Debug</td>-->
        </tr>
    </tbody></table>
</div>

    <div class="pcrs-modal-trace" id="visualizerModal" aria-hidden="true">
    <div class="pcrs-modal-trace-content">
        <div class="pcrs-modal-body">
                <div id="visualize-code">

	            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close</button>
            <div><font size="1"><i>Visualization courtesy <a href="http://www.pythontutor.com/">Phil Guo</a></i></font></div>
        </div>

    </div>
</div>

    

<div class="pcrs-modal-trace" id="waitingModal" aria-hidden="false" style="">
  <div class="pcrs-modal-dialog">
    <div class="pcrs-modal-content" style="margin-top:20%;">
      <div class="pcrs-modal-header">
        <h4 class="pcrs-modal-title">Loading…</h4>
      </div>
      <div class="pcrs-modal-body" align="center">
        <p>Processing code, please wait…</p>
        <img src="/108_20249/static/problems/img/loading.gif" alt="Loading" height="42" width="42">
      </div>
    </div>
  </div>
</div>




    
                
            </div>
            
        
    
        
            
                
                    
                        <div id="python-486" class="code-mirror-wrapper">
                    
                    
                    
    <h3>
        
            
                <p class="widget_title">
                    7 - range #12
                </p>
            
        

        

        
            <span class="problem-score" id="score-python-486"><span title="Progress so far: not attempted" class="align-right" data-reactid=".b"><span data-reactid=".b.0"><sup data-reactid=".b.0.0">-</sup><span data-reactid=".b.0.1">/</span><sub data-reactid=".b.0.2">2</sub></span></span></span>
        

    </h3>



    <div>
        
            
                
                    <h5 class="problem-description">Run the code. The extra `2` in the call to `range()` means that we're going to output only every second number. Change the code to output:<br><br><tt>[1, 3, 5, 7]</tt></h5>
                
            
        
    </div>
    <br>



    

    
        
            
            

<form method="post"> <input type="hidden" name="csrfmiddlewaretoken" value="bcQS6lRS0TePAXBSBabSwukxqoGXhs5uoFauoa1p2YQLyx5PYmZKxRDM8Xj2tbfc"> <fieldset> <ul class="nav nav-tabs tabbed-code-mirror" style="display: none;"><li class="active"><a data-toggle="tab" href="#"></a></li></ul><div class="tab-content"><div class="CodeMirror cm-s-0 cm-s- CodeMirror-wrap tab-pane active"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 8.63623px; left: 39.6591px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none; font-size: 4px;"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 29px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 29px; min-height: 53.9835px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span class="cm-builtin">p</span><span class="cm-builtin">r</span><span class="cm-builtin">i</span><span class="cm-builtin">n</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">l</span><span class="cm-builtin">i</span><span class="cm-builtin">s</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">r</span><span class="cm-builtin">a</span><span class="cm-builtin">n</span><span class="cm-builtin">g</span><span class="cm-builtin">e</span><span>(</span><span class="cm-number">1</span><span>,</span><span> </span><span class="cm-number">6</span><span>,</span><span> </span><span class="cm-number">2</span><span>)</span><span>)</span><span>)</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div class="hash-start" style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">1</div></div><pre><span class="cm-builtin">print</span>(<span class="cm-builtin">list</span>(<span class="cm-builtin">range</span>(<span class="cm-number">1</span>, <span class="cm-number">6</span>, <span class="cm-number">2</span>)))</pre></div><div style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">2</div></div><pre>&nbsp;</pre></div></div><div class="CodeMirror-cursor" style="left: 10px; top: 1.9834px; height: 15.8678px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 53.9835px;"></div><div class="CodeMirror-gutters" style="left: 0.0020751px; height: 54px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 28px;"></div></div></div></div></div> </fieldset>
<div> <button class="btn reg-button" data-target="#history_window_python-486" data-toggle="modal" name="history" type="button">History</button>
<input type="submit" name="Submit" value="Submit" class="btn btn-primary green-button pull-right" id="submit-id-submit">

</div> </form>

        
    

    
        <br>
        <div class="alert-container" id="alert">
            <icon class=""></icon>
            <span></span>
            <a class="at screen-reader-text" href=""></a>
        </div>
    

    
        
<div class="pcrs-modal-history" id="history_window_python-486" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="pcrs-modal-content">
        <div class="pcrs-modal-header">
            <h4 class="pcrs-modal-title" id="myModalLabel" title="7 - range #12 History">
                
                    7 - range #12 History
                
            </h4>
                <button type="button" class="x-button-right" data-dismiss="modal" aria-hidden="false" title="Close History"></button>
        </div>
        <div class="pcrs-modal-body">
            <div class="pcrs-panel-group" id="history_accordion">

            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close
                <span class="at"> Close History </span>
            </button>
        </div>
    </div>
</div>


    

    
    <div id="grade-code" style="display: none;">
    <table id="gradeMatrix" class="pcrs-table">
        <tbody><tr class="pcrs-table-head-row">
            <td class="description">Description</td>
            <td class="expression">Test Expression</td>
            <td class="expected">Expected</td>
            <td class="result">Received</td>
            <td class="passed">Result</td>
            <!--<td class="debug">Debug</td>-->
        </tr>
    </tbody></table>
</div>

    <div class="pcrs-modal-trace" id="visualizerModal" aria-hidden="true">
    <div class="pcrs-modal-trace-content">
        <div class="pcrs-modal-body">
                <div id="visualize-code">

	            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close</button>
            <div><font size="1"><i>Visualization courtesy <a href="http://www.pythontutor.com/">Phil Guo</a></i></font></div>
        </div>

    </div>
</div>

    

<div class="pcrs-modal-trace" id="waitingModal" aria-hidden="false" style="">
  <div class="pcrs-modal-dialog">
    <div class="pcrs-modal-content" style="margin-top:20%;">
      <div class="pcrs-modal-header">
        <h4 class="pcrs-modal-title">Loading…</h4>
      </div>
      <div class="pcrs-modal-body" align="center">
        <p>Processing code, please wait…</p>
        <img src="/108_20249/static/problems/img/loading.gif" alt="Loading" height="42" width="42">
      </div>
    </div>
  </div>
</div>




    
                
            </div>
            
        
    
        
            
                
                    
                        <div id="python-487" class="code-mirror-wrapper">
                    
                    
                    
    <h3>
        
            
                <p class="widget_title">
                    7 - range #13
                </p>
            
        

        

        
            <span class="problem-score" id="score-python-487"><span title="Progress so far: not attempted" class="align-right" data-reactid=".c"><span data-reactid=".c.0"><sup data-reactid=".c.0.0">-</sup><span data-reactid=".c.0.1">/</span><sub data-reactid=".c.0.2">2</sub></span></span></span>
        

    </h3>



    <div>
        
            
                
                    <h5 class="problem-description">Run the code. The extra `2` in the call to `range()` means that we're going to output only every second number. Change the code to output:<br><br><tt>[1, 3, 5, 7]</tt></h5>
                
            
        
    </div>
    <br>



    

    
        
            
            

<form method="post"> <input type="hidden" name="csrfmiddlewaretoken" value="bcQS6lRS0TePAXBSBabSwukxqoGXhs5uoFauoa1p2YQLyx5PYmZKxRDM8Xj2tbfc"> <fieldset> <ul class="nav nav-tabs tabbed-code-mirror" style="display: none;"><li class="active"><a data-toggle="tab" href="#"></a></li></ul><div class="tab-content"><div class="CodeMirror cm-s-0 cm-s- CodeMirror-wrap tab-pane active"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 8.63647px; left: 39.6591px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none; font-size: 4px;"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 29px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 29px; min-height: 53.9835px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span class="cm-builtin">p</span><span class="cm-builtin">r</span><span class="cm-builtin">i</span><span class="cm-builtin">n</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">l</span><span class="cm-builtin">i</span><span class="cm-builtin">s</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">r</span><span class="cm-builtin">a</span><span class="cm-builtin">n</span><span class="cm-builtin">g</span><span class="cm-builtin">e</span><span>(</span><span class="cm-number">1</span><span>,</span><span> </span><span class="cm-number">6</span><span>,</span><span> </span><span class="cm-number">2</span><span>)</span><span>)</span><span>)</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div class="hash-start" style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">1</div></div><pre><span class="cm-builtin">print</span>(<span class="cm-builtin">list</span>(<span class="cm-builtin">range</span>(<span class="cm-number">1</span>, <span class="cm-number">6</span>, <span class="cm-number">2</span>)))</pre></div><div style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">2</div></div><pre>&nbsp;</pre></div></div><div class="CodeMirror-cursor" style="left: 10px; top: 1.9834px; height: 15.8678px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 53.9835px;"></div><div class="CodeMirror-gutters" style="left: 0.0020751px; height: 54px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 28px;"></div></div></div></div></div> </fieldset>
<div> <button class="btn reg-button" data-target="#history_window_python-487" data-toggle="modal" name="history" type="button">History</button>
<input type="submit" name="Submit" value="Submit" class="btn btn-primary green-button pull-right" id="submit-id-submit">

</div> </form>

        
    

    
        <br>
        <div class="alert-container" id="alert">
            <icon class=""></icon>
            <span></span>
            <a class="at screen-reader-text" href=""></a>
        </div>
    

    
        
<div class="pcrs-modal-history" id="history_window_python-487" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="pcrs-modal-content">
        <div class="pcrs-modal-header">
            <h4 class="pcrs-modal-title" id="myModalLabel" title="7 - range #13 History">
                
                    7 - range #13 History
                
            </h4>
                <button type="button" class="x-button-right" data-dismiss="modal" aria-hidden="false" title="Close History"></button>
        </div>
        <div class="pcrs-modal-body">
            <div class="pcrs-panel-group" id="history_accordion">

            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close
                <span class="at"> Close History </span>
            </button>
        </div>
    </div>
</div>


    

    
    <div id="grade-code" style="display: none;">
    <table id="gradeMatrix" class="pcrs-table">
        <tbody><tr class="pcrs-table-head-row">
            <td class="description">Description</td>
            <td class="expression">Test Expression</td>
            <td class="expected">Expected</td>
            <td class="result">Received</td>
            <td class="passed">Result</td>
            <!--<td class="debug">Debug</td>-->
        </tr>
    </tbody></table>
</div>

    <div class="pcrs-modal-trace" id="visualizerModal" aria-hidden="true">
    <div class="pcrs-modal-trace-content">
        <div class="pcrs-modal-body">
                <div id="visualize-code">

	            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close</button>
            <div><font size="1"><i>Visualization courtesy <a href="http://www.pythontutor.com/">Phil Guo</a></i></font></div>
        </div>

    </div>
</div>

    

<div class="pcrs-modal-trace" id="waitingModal" aria-hidden="false" style="">
  <div class="pcrs-modal-dialog">
    <div class="pcrs-modal-content" style="margin-top:20%;">
      <div class="pcrs-modal-header">
        <h4 class="pcrs-modal-title">Loading…</h4>
      </div>
      <div class="pcrs-modal-body" align="center">
        <p>Processing code, please wait…</p>
        <img src="/108_20249/static/problems/img/loading.gif" alt="Loading" height="42" width="42">
      </div>
    </div>
  </div>
</div>




    
                
            </div>
            
        
    
        
            
                
                    
                        <div id="python-488" class="code-mirror-wrapper">
                    
                    
                    
    <h3>
        
            
                <p class="widget_title">
                    7 - range #14
                </p>
            
        

        

        
            <span class="problem-score" id="score-python-488"><span title="Progress so far: not attempted" class="align-right" data-reactid=".d"><span data-reactid=".d.0"><sup data-reactid=".d.0.0">-</sup><span data-reactid=".d.0.1">/</span><sub data-reactid=".d.0.2">2</sub></span></span></span>
        

    </h3>



    <div>
        
            
                
                    <h5 class="problem-description">Change the code to output:<br><br><tt>[2, 4, 6, 8, 10]</tt></h5>
                
            
        
    </div>
    <br>



    

    
        
            
            

<form method="post"> <input type="hidden" name="csrfmiddlewaretoken" value="bcQS6lRS0TePAXBSBabSwukxqoGXhs5uoFauoa1p2YQLyx5PYmZKxRDM8Xj2tbfc"> <fieldset> <ul class="nav nav-tabs tabbed-code-mirror" style="display: none;"><li class="active"><a data-toggle="tab" href="#"></a></li></ul><div class="tab-content"><div class="CodeMirror cm-s-0 cm-s- CodeMirror-wrap tab-pane active"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 8.63647px; left: 39.6591px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none; font-size: 4px;"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 29px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 29px; min-height: 53.9835px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span class="cm-builtin">p</span><span class="cm-builtin">r</span><span class="cm-builtin">i</span><span class="cm-builtin">n</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">l</span><span class="cm-builtin">i</span><span class="cm-builtin">s</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">r</span><span class="cm-builtin">a</span><span class="cm-builtin">n</span><span class="cm-builtin">g</span><span class="cm-builtin">e</span><span>(</span><span class="cm-number">2</span><span>,</span><span> </span><span class="cm-number">1</span><span class="cm-number">0</span><span>,</span><span> </span><span class="cm-number">2</span><span>)</span><span>)</span><span>)</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div class="hash-start" style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">1</div></div><pre><span class="cm-builtin">print</span>(<span class="cm-builtin">list</span>(<span class="cm-builtin">range</span>(<span class="cm-number">2</span>, <span class="cm-number">10</span>, <span class="cm-number">2</span>)))</pre></div><div style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">2</div></div><pre>&nbsp;</pre></div></div><div class="CodeMirror-cursor" style="left: 10px; top: 1.9834px; height: 15.8678px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 53.9835px;"></div><div class="CodeMirror-gutters" style="left: 0.0020751px; height: 54px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 28px;"></div></div></div></div></div> </fieldset>
<div> <button class="btn reg-button" data-target="#history_window_python-488" data-toggle="modal" name="history" type="button">History</button>
<input type="submit" name="Submit" value="Submit" class="btn btn-primary green-button pull-right" id="submit-id-submit">

</div> </form>

        
    

    
        <br>
        <div class="alert-container" id="alert">
            <icon class=""></icon>
            <span></span>
            <a class="at screen-reader-text" href=""></a>
        </div>
    

    
        
<div class="pcrs-modal-history" id="history_window_python-488" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="pcrs-modal-content">
        <div class="pcrs-modal-header">
            <h4 class="pcrs-modal-title" id="myModalLabel" title="7 - range #14 History">
                
                    7 - range #14 History
                
            </h4>
                <button type="button" class="x-button-right" data-dismiss="modal" aria-hidden="false" title="Close History"></button>
        </div>
        <div class="pcrs-modal-body">
            <div class="pcrs-panel-group" id="history_accordion">

            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close
                <span class="at"> Close History </span>
            </button>
        </div>
    </div>
</div>


    

    
    <div id="grade-code" style="display: none;">
    <table id="gradeMatrix" class="pcrs-table">
        <tbody><tr class="pcrs-table-head-row">
            <td class="description">Description</td>
            <td class="expression">Test Expression</td>
            <td class="expected">Expected</td>
            <td class="result">Received</td>
            <td class="passed">Result</td>
            <!--<td class="debug">Debug</td>-->
        </tr>
    </tbody></table>
</div>

    <div class="pcrs-modal-trace" id="visualizerModal" aria-hidden="true">
    <div class="pcrs-modal-trace-content">
        <div class="pcrs-modal-body">
                <div id="visualize-code">

	            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close</button>
            <div><font size="1"><i>Visualization courtesy <a href="http://www.pythontutor.com/">Phil Guo</a></i></font></div>
        </div>

    </div>
</div>

    

<div class="pcrs-modal-trace" id="waitingModal" aria-hidden="false" style="">
  <div class="pcrs-modal-dialog">
    <div class="pcrs-modal-content" style="margin-top:20%;">
      <div class="pcrs-modal-header">
        <h4 class="pcrs-modal-title">Loading…</h4>
      </div>
      <div class="pcrs-modal-body" align="center">
        <p>Processing code, please wait…</p>
        <img src="/108_20249/static/problems/img/loading.gif" alt="Loading" height="42" width="42">
      </div>
    </div>
  </div>
</div>




    
                
            </div>
            
        
    
        
            
                
                    
                        <div id="python-489" class="code-mirror-wrapper">
                    
                    
                    
    <h3>
        
            
                <p class="widget_title">
                    7 - range #15
                </p>
            
        

        

        
            <span class="problem-score" id="score-python-489"><span title="Progress so far: not attempted" class="align-right" data-reactid=".e"><span data-reactid=".e.0"><sup data-reactid=".e.0.0">-</sup><span data-reactid=".e.0.1">/</span><sub data-reactid=".e.0.2">2</sub></span></span></span>
        

    </h3>



    <div>
        
            
                
                    <h5 class="problem-description">Change the code to output:<br><br><tt>[1, 3, 5]</tt></h5>
                
            
        
    </div>
    <br>



    

    
        
            
            

<form method="post"> <input type="hidden" name="csrfmiddlewaretoken" value="bcQS6lRS0TePAXBSBabSwukxqoGXhs5uoFauoa1p2YQLyx5PYmZKxRDM8Xj2tbfc"> <fieldset> <ul class="nav nav-tabs tabbed-code-mirror" style="display: none;"><li class="active"><a data-toggle="tab" href="#"></a></li></ul><div class="tab-content"><div class="CodeMirror cm-s-0 cm-s- CodeMirror-wrap tab-pane active"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 8.63623px; left: 39.6591px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none; font-size: 4px;"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 29px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 29px; min-height: 53.9835px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span class="cm-builtin">p</span><span class="cm-builtin">r</span><span class="cm-builtin">i</span><span class="cm-builtin">n</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">l</span><span class="cm-builtin">i</span><span class="cm-builtin">s</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">r</span><span class="cm-builtin">a</span><span class="cm-builtin">n</span><span class="cm-builtin">g</span><span class="cm-builtin">e</span><span>(</span><span class="cm-number">2</span><span>,</span><span> </span><span class="cm-number">1</span><span class="cm-number">0</span><span>,</span><span> </span><span class="cm-number">2</span><span>)</span><span>)</span><span>)</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div class="hash-start" style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">1</div></div><pre><span class="cm-builtin">print</span>(<span class="cm-builtin">list</span>(<span class="cm-builtin">range</span>(<span class="cm-number">2</span>, <span class="cm-number">10</span>, <span class="cm-number">2</span>)))</pre></div><div style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">2</div></div><pre>&nbsp;</pre></div></div><div class="CodeMirror-cursor" style="left: 10px; top: 1.9834px; height: 15.8678px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 53.9835px;"></div><div class="CodeMirror-gutters" style="left: 0.0020751px; height: 54px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 28px;"></div></div></div></div></div> </fieldset>
<div> <button class="btn reg-button" data-target="#history_window_python-489" data-toggle="modal" name="history" type="button">History</button>
<input type="submit" name="Submit" value="Submit" class="btn btn-primary green-button pull-right" id="submit-id-submit">

</div> </form>

        
    

    
        <br>
        <div class="alert-container" id="alert">
            <icon class=""></icon>
            <span></span>
            <a class="at screen-reader-text" href=""></a>
        </div>
    

    
        
<div class="pcrs-modal-history" id="history_window_python-489" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="pcrs-modal-content">
        <div class="pcrs-modal-header">
            <h4 class="pcrs-modal-title" id="myModalLabel" title="7 - range #15 History">
                
                    7 - range #15 History
                
            </h4>
                <button type="button" class="x-button-right" data-dismiss="modal" aria-hidden="false" title="Close History"></button>
        </div>
        <div class="pcrs-modal-body">
            <div class="pcrs-panel-group" id="history_accordion">

            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close
                <span class="at"> Close History </span>
            </button>
        </div>
    </div>
</div>


    

    
    <div id="grade-code" style="display: none;">
    <table id="gradeMatrix" class="pcrs-table">
        <tbody><tr class="pcrs-table-head-row">
            <td class="description">Description</td>
            <td class="expression">Test Expression</td>
            <td class="expected">Expected</td>
            <td class="result">Received</td>
            <td class="passed">Result</td>
            <!--<td class="debug">Debug</td>-->
        </tr>
    </tbody></table>
</div>

    <div class="pcrs-modal-trace" id="visualizerModal" aria-hidden="true">
    <div class="pcrs-modal-trace-content">
        <div class="pcrs-modal-body">
                <div id="visualize-code">

	            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close</button>
            <div><font size="1"><i>Visualization courtesy <a href="http://www.pythontutor.com/">Phil Guo</a></i></font></div>
        </div>

    </div>
</div>

    

<div class="pcrs-modal-trace" id="waitingModal" aria-hidden="false" style="">
  <div class="pcrs-modal-dialog">
    <div class="pcrs-modal-content" style="margin-top:20%;">
      <div class="pcrs-modal-header">
        <h4 class="pcrs-modal-title">Loading…</h4>
      </div>
      <div class="pcrs-modal-body" align="center">
        <p>Processing code, please wait…</p>
        <img src="/108_20249/static/problems/img/loading.gif" alt="Loading" height="42" width="42">
      </div>
    </div>
  </div>
</div>




    
                
            </div>
            
        
    
        
            
                
                    
                        <div id="python-490" class="code-mirror-wrapper">
                    
                    
                    
    <h3>
        
            
                <p class="widget_title">
                    7 - range #16
                </p>
            
        

        

        
            <span class="problem-score" id="score-python-490"><span title="Progress so far: complete" class="align-right" data-reactid=".f"><span class="green-checkmark-icon" data-reactid=".f.0"></span></span></span>
        

    </h3>



    <div>
        
            
                
                    <h5 class="problem-description">Change the code to output:<br><br><tt>[1, 4, 7, 10]</tt><br><br>Note: the `3` in the argument list for `range()` means that it will output every third number.</h5>
                
            
        
    </div>
    <br>



    

    
        
            
            

<form method="post"> <input type="hidden" name="csrfmiddlewaretoken" value="bcQS6lRS0TePAXBSBabSwukxqoGXhs5uoFauoa1p2YQLyx5PYmZKxRDM8Xj2tbfc"> <fieldset> <ul class="nav nav-tabs tabbed-code-mirror" style="display: none;"><li class="active"><a data-toggle="tab" href="#"></a></li></ul><div class="tab-content"><div class="CodeMirror cm-s-0 cm-s- CodeMirror-wrap tab-pane active"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 8.63623px; left: 39.6591px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none; font-size: 4px;"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 29px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 29px; min-height: 53.9835px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span class="cm-builtin">p</span><span class="cm-builtin">r</span><span class="cm-builtin">i</span><span class="cm-builtin">n</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">l</span><span class="cm-builtin">i</span><span class="cm-builtin">s</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">r</span><span class="cm-builtin">a</span><span class="cm-builtin">n</span><span class="cm-builtin">g</span><span class="cm-builtin">e</span><span>(</span><span class="cm-number">2</span><span>,</span><span> </span><span class="cm-number">1</span><span class="cm-number">0</span><span>,</span><span> </span><span class="cm-number">3</span><span>)</span><span>)</span><span>)</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div class="hash-start" style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">1</div></div><pre><span class="cm-builtin">print</span>(<span class="cm-builtin">list</span>(<span class="cm-builtin">range</span>(<span class="cm-number">2</span>, <span class="cm-number">10</span>, <span class="cm-number">3</span>)))</pre></div><div style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">2</div></div><pre>&nbsp;</pre></div></div><div class="CodeMirror-cursor" style="left: 10px; top: 1.9834px; height: 15.8678px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 53.9835px;"></div><div class="CodeMirror-gutters" style="left: 0.0020751px; height: 54px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 28px;"></div></div></div></div></div> </fieldset>
<div> <button class="btn reg-button" data-target="#history_window_python-490" data-toggle="modal" name="history" type="button">History</button>
<input type="submit" name="Submit" value="Submit" class="btn btn-primary green-button pull-right" id="submit-id-submit">

</div> </form>

        
    

    
        <br>
        <div class="alert-container" id="alert">
            <icon class=""></icon>
            <span></span>
            <a class="at screen-reader-text" href=""></a>
        </div>
    

    
        
<div class="pcrs-modal-history" id="history_window_python-490" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="pcrs-modal-content">
        <div class="pcrs-modal-header">
            <h4 class="pcrs-modal-title" id="myModalLabel" title="7 - range #16 History">
                
                    7 - range #16 History
                
            </h4>
                <button type="button" class="x-button-right" data-dismiss="modal" aria-hidden="false" title="Close History"></button>
        </div>
        <div class="pcrs-modal-body">
            <div class="pcrs-panel-group" id="history_accordion">

            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close
                <span class="at"> Close History </span>
            </button>
        </div>
    </div>
</div>


    

    
    <div id="grade-code" style="display: none;">
    <table id="gradeMatrix" class="pcrs-table">
        <tbody><tr class="pcrs-table-head-row">
            <td class="description">Description</td>
            <td class="expression">Test Expression</td>
            <td class="expected">Expected</td>
            <td class="result">Received</td>
            <td class="passed">Result</td>
            <!--<td class="debug">Debug</td>-->
        </tr>
    </tbody></table>
</div>

    <div class="pcrs-modal-trace" id="visualizerModal" aria-hidden="true">
    <div class="pcrs-modal-trace-content">
        <div class="pcrs-modal-body">
                <div id="visualize-code">

	            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close</button>
            <div><font size="1"><i>Visualization courtesy <a href="http://www.pythontutor.com/">Phil Guo</a></i></font></div>
        </div>

    </div>
</div>

    

<div class="pcrs-modal-trace" id="waitingModal" aria-hidden="false" style="">
  <div class="pcrs-modal-dialog">
    <div class="pcrs-modal-content" style="margin-top:20%;">
      <div class="pcrs-modal-header">
        <h4 class="pcrs-modal-title">Loading…</h4>
      </div>
      <div class="pcrs-modal-body" align="center">
        <p>Processing code, please wait…</p>
        <img src="/108_20249/static/problems/img/loading.gif" alt="Loading" height="42" width="42">
      </div>
    </div>
  </div>
</div>




    
                
            </div>
            
        
    
        
            
                
                    
                        <div id="python-491" class="code-mirror-wrapper">
                    
                    
                    
    <h3>
        
            
                <p class="widget_title">
                    7 - range #17
                </p>
            
        

        

        
            <span class="problem-score" id="score-python-491"><span title="Progress so far: not attempted" class="align-right" data-reactid=".g"><span data-reactid=".g.0"><sup data-reactid=".g.0.0">-</sup><span data-reactid=".g.0.1">/</span><sub data-reactid=".g.0.2">2</sub></span></span></span>
        

    </h3>



    <div>
        
            
                
                    <h5 class="problem-description">Change the code to output:<br><br><tt>[0, 10, 20, 30, 40]</tt><br><br>Hint: you'll change the 3 to something else. Do not change any other number.</h5>
                
            
        
    </div>
    <br>



    

    
        
            
            

<form method="post"> <input type="hidden" name="csrfmiddlewaretoken" value="bcQS6lRS0TePAXBSBabSwukxqoGXhs5uoFauoa1p2YQLyx5PYmZKxRDM8Xj2tbfc"> <fieldset> <ul class="nav nav-tabs tabbed-code-mirror" style="display: none;"><li class="active"><a data-toggle="tab" href="#"></a></li></ul><div class="tab-content"><div class="CodeMirror cm-s-0 cm-s- CodeMirror-wrap tab-pane active"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 8.63672px; left: 39.6591px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none; font-size: 4px;"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 29px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 29px; min-height: 53.9835px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span class="cm-builtin">p</span><span class="cm-builtin">r</span><span class="cm-builtin">i</span><span class="cm-builtin">n</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">l</span><span class="cm-builtin">i</span><span class="cm-builtin">s</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">r</span><span class="cm-builtin">a</span><span class="cm-builtin">n</span><span class="cm-builtin">g</span><span class="cm-builtin">e</span><span>(</span><span class="cm-number">0</span><span>,</span><span> </span><span class="cm-number">4</span><span class="cm-number">1</span><span>,</span><span> </span><span class="cm-number">3</span><span>)</span><span>)</span><span>)</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div class="hash-start" style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">1</div></div><pre><span class="cm-builtin">print</span>(<span class="cm-builtin">list</span>(<span class="cm-builtin">range</span>(<span class="cm-number">0</span>, <span class="cm-number">41</span>, <span class="cm-number">3</span>)))</pre></div><div style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">2</div></div><pre>&nbsp;</pre></div></div><div class="CodeMirror-cursor" style="left: 10px; top: 1.9834px; height: 15.8678px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 53.9835px;"></div><div class="CodeMirror-gutters" style="left: 0.0020751px; height: 54px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 28px;"></div></div></div></div></div> </fieldset>
<div> <button class="btn reg-button" data-target="#history_window_python-491" data-toggle="modal" name="history" type="button">History</button>
<input type="submit" name="Submit" value="Submit" class="btn btn-primary green-button pull-right" id="submit-id-submit">

</div> </form>

        
    

    
        <br>
        <div class="alert-container" id="alert">
            <icon class=""></icon>
            <span></span>
            <a class="at screen-reader-text" href=""></a>
        </div>
    

    
        
<div class="pcrs-modal-history" id="history_window_python-491" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="pcrs-modal-content">
        <div class="pcrs-modal-header">
            <h4 class="pcrs-modal-title" id="myModalLabel" title="7 - range #17 History">
                
                    7 - range #17 History
                
            </h4>
                <button type="button" class="x-button-right" data-dismiss="modal" aria-hidden="false" title="Close History"></button>
        </div>
        <div class="pcrs-modal-body">
            <div class="pcrs-panel-group" id="history_accordion">

            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close
                <span class="at"> Close History </span>
            </button>
        </div>
    </div>
</div>


    

    
    <div id="grade-code" style="display: none;">
    <table id="gradeMatrix" class="pcrs-table">
        <tbody><tr class="pcrs-table-head-row">
            <td class="description">Description</td>
            <td class="expression">Test Expression</td>
            <td class="expected">Expected</td>
            <td class="result">Received</td>
            <td class="passed">Result</td>
            <!--<td class="debug">Debug</td>-->
        </tr>
    </tbody></table>
</div>

    <div class="pcrs-modal-trace" id="visualizerModal" aria-hidden="true">
    <div class="pcrs-modal-trace-content">
        <div class="pcrs-modal-body">
                <div id="visualize-code">

	            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close</button>
            <div><font size="1"><i>Visualization courtesy <a href="http://www.pythontutor.com/">Phil Guo</a></i></font></div>
        </div>

    </div>
</div>

    

<div class="pcrs-modal-trace" id="waitingModal" aria-hidden="false" style="">
  <div class="pcrs-modal-dialog">
    <div class="pcrs-modal-content" style="margin-top:20%;">
      <div class="pcrs-modal-header">
        <h4 class="pcrs-modal-title">Loading…</h4>
      </div>
      <div class="pcrs-modal-body" align="center">
        <p>Processing code, please wait…</p>
        <img src="/108_20249/static/problems/img/loading.gif" alt="Loading" height="42" width="42">
      </div>
    </div>
  </div>
</div>




    
                
            </div>
            
        
    
        
            
                
                    
                        <div id="python-492" class="code-mirror-wrapper">
                    
                    
                    
    <h3>
        
            
                <p class="widget_title">
                    7 - range #18
                </p>
            
        

        

        
            <span class="problem-score" id="score-python-492"><span title="Progress so far: not attempted" class="align-right" data-reactid=".h"><span data-reactid=".h.0"><sup data-reactid=".h.0.0">-</sup><span data-reactid=".h.0.1">/</span><sub data-reactid=".h.0.2">2</sub></span></span></span>
        

    </h3>



    <div>
        
            
                
                    <h5 class="problem-description">Change the code to output<br><br><tt>[0, 1, 2, 3, 4, 5]</tt></h5>
                
            
        
    </div>
    <br>



    

    
        
            
            

<form method="post"> <input type="hidden" name="csrfmiddlewaretoken" value="bcQS6lRS0TePAXBSBabSwukxqoGXhs5uoFauoa1p2YQLyx5PYmZKxRDM8Xj2tbfc"> <fieldset> <ul class="nav nav-tabs tabbed-code-mirror" style="display: none;"><li class="active"><a data-toggle="tab" href="#"></a></li></ul><div class="tab-content"><div class="CodeMirror cm-s-0 cm-s- CodeMirror-wrap tab-pane active"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 8.63623px; left: 39.6591px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none; font-size: 4px;"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 29px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 29px; min-height: 53.9835px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span class="cm-builtin">p</span><span class="cm-builtin">r</span><span class="cm-builtin">i</span><span class="cm-builtin">n</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">l</span><span class="cm-builtin">i</span><span class="cm-builtin">s</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">r</span><span class="cm-builtin">a</span><span class="cm-builtin">n</span><span class="cm-builtin">g</span><span class="cm-builtin">e</span><span>(</span><span class="cm-number">5</span><span>)</span><span>)</span><span>)</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div class="hash-start" style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">1</div></div><pre><span class="cm-builtin">print</span>(<span class="cm-builtin">list</span>(<span class="cm-builtin">range</span>(<span class="cm-number">5</span>)))</pre></div><div style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">2</div></div><pre>&nbsp;</pre></div></div><div class="CodeMirror-cursor" style="left: 10px; top: 1.9834px; height: 15.8678px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 53.9835px;"></div><div class="CodeMirror-gutters" style="left: 0.0020751px; height: 54px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 28px;"></div></div></div></div></div> </fieldset>
<div> <button class="btn reg-button" data-target="#history_window_python-492" data-toggle="modal" name="history" type="button">History</button>
<input type="submit" name="Submit" value="Submit" class="btn btn-primary green-button pull-right" id="submit-id-submit">

</div> </form>

        
    

    
        <br>
        <div class="alert-container" id="alert">
            <icon class=""></icon>
            <span></span>
            <a class="at screen-reader-text" href=""></a>
        </div>
    

    
        
<div class="pcrs-modal-history" id="history_window_python-492" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="pcrs-modal-content">
        <div class="pcrs-modal-header">
            <h4 class="pcrs-modal-title" id="myModalLabel" title="7 - range #18 History">
                
                    7 - range #18 History
                
            </h4>
                <button type="button" class="x-button-right" data-dismiss="modal" aria-hidden="false" title="Close History"></button>
        </div>
        <div class="pcrs-modal-body">
            <div class="pcrs-panel-group" id="history_accordion">

            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close
                <span class="at"> Close History </span>
            </button>
        </div>
    </div>
</div>


    

    
    <div id="grade-code" style="display: none;">
    <table id="gradeMatrix" class="pcrs-table">
        <tbody><tr class="pcrs-table-head-row">
            <td class="description">Description</td>
            <td class="expression">Test Expression</td>
            <td class="expected">Expected</td>
            <td class="result">Received</td>
            <td class="passed">Result</td>
            <!--<td class="debug">Debug</td>-->
        </tr>
    </tbody></table>
</div>

    <div class="pcrs-modal-trace" id="visualizerModal" aria-hidden="true">
    <div class="pcrs-modal-trace-content">
        <div class="pcrs-modal-body">
                <div id="visualize-code">

	            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close</button>
            <div><font size="1"><i>Visualization courtesy <a href="http://www.pythontutor.com/">Phil Guo</a></i></font></div>
        </div>

    </div>
</div>

    

<div class="pcrs-modal-trace" id="waitingModal" aria-hidden="false" style="">
  <div class="pcrs-modal-dialog">
    <div class="pcrs-modal-content" style="margin-top:20%;">
      <div class="pcrs-modal-header">
        <h4 class="pcrs-modal-title">Loading…</h4>
      </div>
      <div class="pcrs-modal-body" align="center">
        <p>Processing code, please wait…</p>
        <img src="/108_20249/static/problems/img/loading.gif" alt="Loading" height="42" width="42">
      </div>
    </div>
  </div>
</div>




    
                
            </div>
            
        
    
        
            
                
                    
                        <div id="python-493" class="code-mirror-wrapper">
                    
                    
                    
    <h3>
        
            
                <p class="widget_title">
                    7 - range #19
                </p>
            
        

        

        
            <span class="problem-score" id="score-python-493"><span title="Progress so far: not attempted" class="align-right" data-reactid=".i"><span data-reactid=".i.0"><sup data-reactid=".i.0.0">-</sup><span data-reactid=".i.0.1">/</span><sub data-reactid=".i.0.2">2</sub></span></span></span>
        

    </h3>



    <div>
        
            
                
                    <h5 class="problem-description">We can pass just one number to `range()` if we want. It will return numbers starting from `0` to the number you give it minus one. Change the code to output<br><br><tt>[0, 1, 2, 3]</tt></h5>
                
            
        
    </div>
    <br>



    

    
        
            
            

<form method="post"> <input type="hidden" name="csrfmiddlewaretoken" value="bcQS6lRS0TePAXBSBabSwukxqoGXhs5uoFauoa1p2YQLyx5PYmZKxRDM8Xj2tbfc"> <fieldset> <ul class="nav nav-tabs tabbed-code-mirror" style="display: none;"><li class="active"><a data-toggle="tab" href="#"></a></li></ul><div class="tab-content"><div class="CodeMirror cm-s-0 cm-s- CodeMirror-wrap tab-pane active"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 8.63672px; left: 39.6591px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none; font-size: 4px;"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 29px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 29px; min-height: 53.9835px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span class="cm-builtin">p</span><span class="cm-builtin">r</span><span class="cm-builtin">i</span><span class="cm-builtin">n</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">l</span><span class="cm-builtin">i</span><span class="cm-builtin">s</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">r</span><span class="cm-builtin">a</span><span class="cm-builtin">n</span><span class="cm-builtin">g</span><span class="cm-builtin">e</span><span>(</span><span class="cm-number">5</span><span>)</span><span>)</span><span>)</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div class="hash-start" style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">1</div></div><pre><span class="cm-builtin">print</span>(<span class="cm-builtin">list</span>(<span class="cm-builtin">range</span>(<span class="cm-number">5</span>)))</pre></div><div style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">2</div></div><pre>&nbsp;</pre></div></div><div class="CodeMirror-cursor" style="left: 10px; top: 1.98389px; height: 15.8678px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 53.9835px;"></div><div class="CodeMirror-gutters" style="left: 0.0020751px; height: 54px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 28px;"></div></div></div></div></div> </fieldset>
<div> <button class="btn reg-button" data-target="#history_window_python-493" data-toggle="modal" name="history" type="button">History</button>
<input type="submit" name="Submit" value="Submit" class="btn btn-primary green-button pull-right" id="submit-id-submit">

</div> </form>

        
    

    
        <br>
        <div class="alert-container" id="alert">
            <icon class=""></icon>
            <span></span>
            <a class="at screen-reader-text" href=""></a>
        </div>
    

    
        
<div class="pcrs-modal-history" id="history_window_python-493" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="pcrs-modal-content">
        <div class="pcrs-modal-header">
            <h4 class="pcrs-modal-title" id="myModalLabel" title="7 - range #19 History">
                
                    7 - range #19 History
                
            </h4>
                <button type="button" class="x-button-right" data-dismiss="modal" aria-hidden="false" title="Close History"></button>
        </div>
        <div class="pcrs-modal-body">
            <div class="pcrs-panel-group" id="history_accordion">

            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close
                <span class="at"> Close History </span>
            </button>
        </div>
    </div>
</div>


    

    
    <div id="grade-code" style="display: none;">
    <table id="gradeMatrix" class="pcrs-table">
        <tbody><tr class="pcrs-table-head-row">
            <td class="description">Description</td>
            <td class="expression">Test Expression</td>
            <td class="expected">Expected</td>
            <td class="result">Received</td>
            <td class="passed">Result</td>
            <!--<td class="debug">Debug</td>-->
        </tr>
    </tbody></table>
</div>

    <div class="pcrs-modal-trace" id="visualizerModal" aria-hidden="true">
    <div class="pcrs-modal-trace-content">
        <div class="pcrs-modal-body">
                <div id="visualize-code">

	            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close</button>
            <div><font size="1"><i>Visualization courtesy <a href="http://www.pythontutor.com/">Phil Guo</a></i></font></div>
        </div>

    </div>
</div>

    

<div class="pcrs-modal-trace" id="waitingModal" aria-hidden="false" style="">
  <div class="pcrs-modal-dialog">
    <div class="pcrs-modal-content" style="margin-top:20%;">
      <div class="pcrs-modal-header">
        <h4 class="pcrs-modal-title">Loading…</h4>
      </div>
      <div class="pcrs-modal-body" align="center">
        <p>Processing code, please wait…</p>
        <img src="/108_20249/static/problems/img/loading.gif" alt="Loading" height="42" width="42">
      </div>
    </div>
  </div>
</div>




    
                
            </div>
            
        
    
        
            
                
                    
                        <div id="python-494" class="code-mirror-wrapper">
                    
                    
                    
    <h3>
        
            
                <p class="widget_title">
                    7 - range #20
                </p>
            
        

        

        
            <span class="problem-score" id="score-python-494"><span title="Progress so far: not attempted" class="align-right" data-reactid=".j"><span data-reactid=".j.0"><sup data-reactid=".j.0.0">-</sup><span data-reactid=".j.0.1">/</span><sub data-reactid=".j.0.2">3</sub></span></span></span>
        

    </h3>



    <div>
        
            
                
                    <h5 class="problem-description">Variable `numbers` stores the output from the `range()` call. Change the code to output<br><br><tt>[0, 1, 2, 3, 4, 5]</tt><br><br>Hint: you'll change the 5. You will not change the `print()` function.</h5>
                
            
        
    </div>
    <br>



    

    
        
            
            

<form method="post"> <input type="hidden" name="csrfmiddlewaretoken" value="bcQS6lRS0TePAXBSBabSwukxqoGXhs5uoFauoa1p2YQLyx5PYmZKxRDM8Xj2tbfc"> <fieldset> <ul class="nav nav-tabs tabbed-code-mirror" style="display: none;"><li class="active"><a data-toggle="tab" href="#"></a></li></ul><div class="tab-content"><div class="CodeMirror cm-s-0 cm-s- CodeMirror-wrap tab-pane active"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 8.63623px; left: 39.6591px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none; font-size: 4px;"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 29px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 29px; min-height: 74.9752px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span class="cm-variable">n</span><span class="cm-variable">u</span><span class="cm-variable">m</span><span class="cm-variable">b</span><span class="cm-variable">e</span><span class="cm-variable">r</span><span class="cm-variable">s</span><span> </span><span>=</span><span> </span><span class="cm-builtin">l</span><span class="cm-builtin">i</span><span class="cm-builtin">s</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">r</span><span class="cm-builtin">a</span><span class="cm-builtin">n</span><span class="cm-builtin">g</span><span class="cm-builtin">e</span><span>(</span><span class="cm-number">5</span><span>)</span><span>)</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div class="hash-start" style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">1</div></div><pre><span class="cm-variable">numbers</span> = <span class="cm-builtin">list</span>(<span class="cm-builtin">range</span>(<span class="cm-number">5</span>))</pre></div><div style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">2</div></div><pre><span class="cm-builtin">print</span>(<span class="cm-variable">numbers</span>)</pre></div><div style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">3</div></div><pre>&nbsp;</pre></div></div><div class="CodeMirror-cursor" style="left: 10px; top: 1.9834px; height: 15.8678px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 74.9752px;"></div><div class="CodeMirror-gutters" style="left: 0.0020751px; height: 75px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 28px;"></div></div></div></div></div> </fieldset>
<div> <button class="btn reg-button" data-target="#history_window_python-494" data-toggle="modal" name="history" type="button">History</button>
<input type="submit" name="Submit" value="Submit" class="btn btn-primary green-button pull-right" id="submit-id-submit">

</div> </form>

        
    

    
        <br>
        <div class="alert-container" id="alert">
            <icon class=""></icon>
            <span></span>
            <a class="at screen-reader-text" href=""></a>
        </div>
    

    
        
<div class="pcrs-modal-history" id="history_window_python-494" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="pcrs-modal-content">
        <div class="pcrs-modal-header">
            <h4 class="pcrs-modal-title" id="myModalLabel" title="7 - range #20 History">
                
                    7 - range #20 History
                
            </h4>
                <button type="button" class="x-button-right" data-dismiss="modal" aria-hidden="false" title="Close History"></button>
        </div>
        <div class="pcrs-modal-body">
            <div class="pcrs-panel-group" id="history_accordion">

            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close
                <span class="at"> Close History </span>
            </button>
        </div>
    </div>
</div>


    

    
    <div id="grade-code" style="display: none;">
    <table id="gradeMatrix" class="pcrs-table">
        <tbody><tr class="pcrs-table-head-row">
            <td class="description">Description</td>
            <td class="expression">Test Expression</td>
            <td class="expected">Expected</td>
            <td class="result">Received</td>
            <td class="passed">Result</td>
            <!--<td class="debug">Debug</td>-->
        </tr>
    </tbody></table>
</div>

    <div class="pcrs-modal-trace" id="visualizerModal" aria-hidden="true">
    <div class="pcrs-modal-trace-content">
        <div class="pcrs-modal-body">
                <div id="visualize-code">

	            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close</button>
            <div><font size="1"><i>Visualization courtesy <a href="http://www.pythontutor.com/">Phil Guo</a></i></font></div>
        </div>

    </div>
</div>

    

<div class="pcrs-modal-trace" id="waitingModal" aria-hidden="false" style="">
  <div class="pcrs-modal-dialog">
    <div class="pcrs-modal-content" style="margin-top:20%;">
      <div class="pcrs-modal-header">
        <h4 class="pcrs-modal-title">Loading…</h4>
      </div>
      <div class="pcrs-modal-body" align="center">
        <p>Processing code, please wait…</p>
        <img src="/108_20249/static/problems/img/loading.gif" alt="Loading" height="42" width="42">
      </div>
    </div>
  </div>
</div>




    
                
            </div>
            
        
    
        
            
                
                    
                        <div id="python-495" class="code-mirror-wrapper">
                    
                    
                    
    <h3>
        
            
                <p class="widget_title">
                    7 - range #21
                </p>
            
        

        

        
            <span class="problem-score" id="score-python-495"><span title="Progress so far: not attempted" class="align-right" data-reactid=".k"><span data-reactid=".k.0"><sup data-reactid=".k.0.0">-</sup><span data-reactid=".k.0.1">/</span><sub data-reactid=".k.0.2">3</sub></span></span></span>
        

    </h3>



    <div>
        
            
                
                    <h5 class="problem-description">Change the code to output<br><br><tt>[0, 1, 2, 3, 4, 5, 6, 7, 8]</tt><br><br>Change only line 1.</h5>
                
            
        
    </div>
    <br>



    

    
        
            
            

<form method="post"> <input type="hidden" name="csrfmiddlewaretoken" value="bcQS6lRS0TePAXBSBabSwukxqoGXhs5uoFauoa1p2YQLyx5PYmZKxRDM8Xj2tbfc"> <fieldset> <ul class="nav nav-tabs tabbed-code-mirror" style="display: none;"><li class="active"><a data-toggle="tab" href="#"></a></li></ul><div class="tab-content"><div class="CodeMirror cm-s-0 cm-s- CodeMirror-wrap tab-pane active"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 8.63623px; left: 39.6591px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none; font-size: 4px;"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 29px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 29px; min-height: 74.9752px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span class="cm-variable">n</span><span class="cm-variable">u</span><span class="cm-variable">m</span><span class="cm-variable">b</span><span class="cm-variable">e</span><span class="cm-variable">r</span><span class="cm-variable">s</span><span> </span><span>=</span><span> </span><span class="cm-builtin">l</span><span class="cm-builtin">i</span><span class="cm-builtin">s</span><span class="cm-builtin">t</span><span>(</span><span class="cm-builtin">r</span><span class="cm-builtin">a</span><span class="cm-builtin">n</span><span class="cm-builtin">g</span><span class="cm-builtin">e</span><span>(</span><span class="cm-number">5</span><span>)</span><span>)</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div class="hash-start" style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">1</div></div><pre><span class="cm-variable">numbers</span> = <span class="cm-builtin">list</span>(<span class="cm-builtin">range</span>(<span class="cm-number">5</span>))</pre></div><div style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">2</div></div><pre><span class="cm-builtin">print</span>(<span class="cm-variable">numbers</span>)</pre></div><div style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">3</div></div><pre>&nbsp;</pre></div></div><div class="CodeMirror-cursor" style="left: 10px; top: 1.9834px; height: 15.8678px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 74.9752px;"></div><div class="CodeMirror-gutters" style="left: 0.0020751px; height: 75px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 28px;"></div></div></div></div></div> </fieldset>
<div> <button class="btn reg-button" data-target="#history_window_python-495" data-toggle="modal" name="history" type="button">History</button>
<input type="submit" name="Submit" value="Submit" class="btn btn-primary green-button pull-right" id="submit-id-submit">

</div> </form>

        
    

    
        <br>
        <div class="alert-container" id="alert">
            <icon class=""></icon>
            <span></span>
            <a class="at screen-reader-text" href=""></a>
        </div>
    

    
        
<div class="pcrs-modal-history" id="history_window_python-495" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="pcrs-modal-content">
        <div class="pcrs-modal-header">
            <h4 class="pcrs-modal-title" id="myModalLabel" title="7 - range #21 History">
                
                    7 - range #21 History
                
            </h4>
                <button type="button" class="x-button-right" data-dismiss="modal" aria-hidden="false" title="Close History"></button>
        </div>
        <div class="pcrs-modal-body">
            <div class="pcrs-panel-group" id="history_accordion">

            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close
                <span class="at"> Close History </span>
            </button>
        </div>
    </div>
</div>


    

    
    <div id="grade-code" style="display: none;">
    <table id="gradeMatrix" class="pcrs-table">
        <tbody><tr class="pcrs-table-head-row">
            <td class="description">Description</td>
            <td class="expression">Test Expression</td>
            <td class="expected">Expected</td>
            <td class="result">Received</td>
            <td class="passed">Result</td>
            <!--<td class="debug">Debug</td>-->
        </tr>
    </tbody></table>
</div>

    <div class="pcrs-modal-trace" id="visualizerModal" aria-hidden="true">
    <div class="pcrs-modal-trace-content">
        <div class="pcrs-modal-body">
                <div id="visualize-code">

	            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close</button>
            <div><font size="1"><i>Visualization courtesy <a href="http://www.pythontutor.com/">Phil Guo</a></i></font></div>
        </div>

    </div>
</div>

    

<div class="pcrs-modal-trace" id="waitingModal" aria-hidden="false" style="">
  <div class="pcrs-modal-dialog">
    <div class="pcrs-modal-content" style="margin-top:20%;">
      <div class="pcrs-modal-header">
        <h4 class="pcrs-modal-title">Loading…</h4>
      </div>
      <div class="pcrs-modal-body" align="center">
        <p>Processing code, please wait…</p>
        <img src="/108_20249/static/problems/img/loading.gif" alt="Loading" height="42" width="42">
      </div>
    </div>
  </div>
</div>




    
                
            </div>
            
        
    
        
            
                
                    
                        <div id="python-496" class="code-mirror-wrapper">
                    
                    
                    
    <h3>
        
            
                <p class="widget_title">
                    7 - range #22
                </p>
            
        

        

        
            <span class="problem-score" id="score-python-496"><span title="Progress so far: not attempted" class="align-right" data-reactid=".l"><span data-reactid=".l.0"><sup data-reactid=".l.0.0">-</sup><span data-reactid=".l.0.1">/</span><sub data-reactid=".l.0.2">3</sub></span></span></span>
        

    </h3>



    <div>
        
            
                
                    <h5 class="problem-description">Change the code to output<br><br><tt>[0, 1, 2, 3, 4, 5, 6, 7, 8]</tt><br><br>using a call to `range()`.<br><br>Hint: you will replace `3` with a call to `range()`.</h5>
                
            
        
    </div>
    <br>



    

    
        
            
            

<form method="post"> <input type="hidden" name="csrfmiddlewaretoken" value="bcQS6lRS0TePAXBSBabSwukxqoGXhs5uoFauoa1p2YQLyx5PYmZKxRDM8Xj2tbfc"> <fieldset> <ul class="nav nav-tabs tabbed-code-mirror" style="display: none;"><li class="active"><a data-toggle="tab" href="#"></a></li></ul><div class="tab-content"><div class="CodeMirror cm-s-0 cm-s- CodeMirror-wrap tab-pane active"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 8.63623px; left: 39.6591px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none; font-size: 4px;"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 29px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 29px; min-height: 74.9752px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span class="cm-variable">n</span><span class="cm-variable">u</span><span class="cm-variable">m</span><span class="cm-variable">b</span><span class="cm-variable">e</span><span class="cm-variable">r</span><span class="cm-variable">s</span><span> </span><span>=</span><span> </span><span class="cm-builtin">l</span><span class="cm-builtin">i</span><span class="cm-builtin">s</span><span class="cm-builtin">t</span><span>(</span><span class="cm-number">3</span><span>)</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div class="hash-start" style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">1</div></div><pre><span class="cm-variable">numbers</span> = <span class="cm-builtin">list</span>(<span class="cm-number">3</span>)</pre></div><div style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">2</div></div><pre><span class="cm-builtin">print</span>(<span class="cm-variable">numbers</span>)</pre></div><div style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">3</div></div><pre>&nbsp;</pre></div></div><div class="CodeMirror-cursor" style="left: 10px; top: 1.9834px; height: 15.8678px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 74.9752px;"></div><div class="CodeMirror-gutters" style="left: 0.0020751px; height: 75px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 28px;"></div></div></div></div></div> </fieldset>
<div> <button class="btn reg-button" data-target="#history_window_python-496" data-toggle="modal" name="history" type="button">History</button>
<input type="submit" name="Submit" value="Submit" class="btn btn-primary green-button pull-right" id="submit-id-submit">

</div> </form>

        
    

    
        <br>
        <div class="alert-container" id="alert">
            <icon class=""></icon>
            <span></span>
            <a class="at screen-reader-text" href=""></a>
        </div>
    

    
        
<div class="pcrs-modal-history" id="history_window_python-496" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="pcrs-modal-content">
        <div class="pcrs-modal-header">
            <h4 class="pcrs-modal-title" id="myModalLabel" title="7 - range #22 History">
                
                    7 - range #22 History
                
            </h4>
                <button type="button" class="x-button-right" data-dismiss="modal" aria-hidden="false" title="Close History"></button>
        </div>
        <div class="pcrs-modal-body">
            <div class="pcrs-panel-group" id="history_accordion">

            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close
                <span class="at"> Close History </span>
            </button>
        </div>
    </div>
</div>


    

    
    <div id="grade-code" style="display: none;">
    <table id="gradeMatrix" class="pcrs-table">
        <tbody><tr class="pcrs-table-head-row">
            <td class="description">Description</td>
            <td class="expression">Test Expression</td>
            <td class="expected">Expected</td>
            <td class="result">Received</td>
            <td class="passed">Result</td>
            <!--<td class="debug">Debug</td>-->
        </tr>
    </tbody></table>
</div>

    <div class="pcrs-modal-trace" id="visualizerModal" aria-hidden="true">
    <div class="pcrs-modal-trace-content">
        <div class="pcrs-modal-body">
                <div id="visualize-code">

	            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close</button>
            <div><font size="1"><i>Visualization courtesy <a href="http://www.pythontutor.com/">Phil Guo</a></i></font></div>
        </div>

    </div>
</div>

    

<div class="pcrs-modal-trace" id="waitingModal" aria-hidden="false" style="">
  <div class="pcrs-modal-dialog">
    <div class="pcrs-modal-content" style="margin-top:20%;">
      <div class="pcrs-modal-header">
        <h4 class="pcrs-modal-title">Loading…</h4>
      </div>
      <div class="pcrs-modal-body" align="center">
        <p>Processing code, please wait…</p>
        <img src="/108_20249/static/problems/img/loading.gif" alt="Loading" height="42" width="42">
      </div>
    </div>
  </div>
</div>




    
                
            </div>
            
        
    
        
            
                
                    
                        <div id="python-497" class="code-mirror-wrapper">
                    
                    
                    
    <h3>
        
            
                <p class="widget_title">
                    7 - range #23
                </p>
            
        

        

        
            <span class="problem-score" id="score-python-497"><span title="Progress so far: not attempted" class="align-right" data-reactid=".m"><span data-reactid=".m.0"><sup data-reactid=".m.0.0">-</sup><span data-reactid=".m.0.1">/</span><sub data-reactid=".m.0.2">3</sub></span></span></span>
        

    </h3>



    <div>
        
            
                
                    <h5 class="problem-description">Add code to line 1 to assign a value to variable `numbers` such that the code outputs the following:<br><br><tt>[0, 1, 2, 3, 4, 5, 6, 7, 8]</tt><br><br>You must use a call to `range()`.<br><br>Hint: see previous exercise if you get stuck.</h5>
                
            
        
    </div>
    <br>



    

    
        
            
            

<form method="post"> <input type="hidden" name="csrfmiddlewaretoken" value="bcQS6lRS0TePAXBSBabSwukxqoGXhs5uoFauoa1p2YQLyx5PYmZKxRDM8Xj2tbfc"> <fieldset> <ul class="nav nav-tabs tabbed-code-mirror" style="display: none;"><li class="active"><a data-toggle="tab" href="#"></a></li></ul><div class="tab-content"><div class="CodeMirror cm-s-0 cm-s- CodeMirror-wrap tab-pane active"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 8.63623px; left: 39.6591px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none; font-size: 4px;"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 29px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 29px; min-height: 53.9835px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span class="cm-builtin">p</span><span class="cm-builtin">r</span><span class="cm-builtin">i</span><span class="cm-builtin">n</span><span class="cm-builtin">t</span><span>(</span><span class="cm-variable">n</span><span class="cm-variable">u</span><span class="cm-variable">m</span><span class="cm-variable">b</span><span class="cm-variable">e</span><span class="cm-variable">r</span><span class="cm-variable">s</span><span>)</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div class="hash-start" style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">1</div></div><pre><span class="cm-builtin">print</span>(<span class="cm-variable">numbers</span>)</pre></div><div style="position: relative;"><div style="position: absolute; left: -28.9979px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">2</div></div><pre>&nbsp;</pre></div></div><div class="CodeMirror-cursor" style="left: 10px; top: 1.9834px; height: 15.8678px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 53.9835px;"></div><div class="CodeMirror-gutters" style="left: 0.0020751px; height: 54px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 28px;"></div></div></div></div></div> </fieldset>
<div> <button class="btn reg-button" data-target="#history_window_python-497" data-toggle="modal" name="history" type="button">History</button>
<input type="submit" name="Submit" value="Submit" class="btn btn-primary green-button pull-right" id="submit-id-submit">

</div> </form>

        
    

    
        <br>
        <div class="alert-container" id="alert">
            <icon class=""></icon>
            <span></span>
            <a class="at screen-reader-text" href=""></a>
        </div>
    

    
        
<div class="pcrs-modal-history" id="history_window_python-497" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="pcrs-modal-content">
        <div class="pcrs-modal-header">
            <h4 class="pcrs-modal-title" id="myModalLabel" title="7 - range #23 History">
                
                    7 - range #23 History
                
            </h4>
                <button type="button" class="x-button-right" data-dismiss="modal" aria-hidden="false" title="Close History"></button>
        </div>
        <div class="pcrs-modal-body">
            <div class="pcrs-panel-group" id="history_accordion">

            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close
                <span class="at"> Close History </span>
            </button>
        </div>
    </div>
</div>


    

    
    <div id="grade-code" style="display: none;">
    <table id="gradeMatrix" class="pcrs-table">
        <tbody><tr class="pcrs-table-head-row">
            <td class="description">Description</td>
            <td class="expression">Test Expression</td>
            <td class="expected">Expected</td>
            <td class="result">Received</td>
            <td class="passed">Result</td>
            <!--<td class="debug">Debug</td>-->
        </tr>
    </tbody></table>
</div>

    <div class="pcrs-modal-trace" id="visualizerModal" aria-hidden="true">
    <div class="pcrs-modal-trace-content">
        <div class="pcrs-modal-body">
                <div id="visualize-code">

	            </div>
        </div>
        <div class="pcrs-modal-footer">
            <button type="button" class="reg-button" data-dismiss="modal">Close</button>
            <div><font size="1"><i>Visualization courtesy <a href="http://www.pythontutor.com/">Phil Guo</a></i></font></div>
        </div>

    </div>
</div>

    

<div class="pcrs-modal-trace" id="waitingModal" aria-hidden="false" style="">
  <div class="pcrs-modal-dialog">
    <div class="pcrs-modal-content" style="margin-top:20%;">
      <div class="pcrs-modal-header">
        <h4 class="pcrs-modal-title">Loading…</h4>
      </div>
      <div class="pcrs-modal-body" align="center">
        <p>Processing code, please wait…</p>
        <img src="/108_20249/static/problems/img/loading.gif" alt="Loading" height="42" width="42">
      </div>
    </div>
  </div>
</div>




    
                
            </div>
            
        
    


    <!-- Create YT.Players when YouTube API is ready -->
    <script>
        function onYouTubeIframeAPIReady() {
            for (i = 0; i < YT_Videos.length; i++) {
                var player = new YT.Player(YT_Videos[i].id,
                    {
                    events: {
                        'onStateChange': YT_Videos[i].onPlayerStateChange }
                    });
                YT_Players.push(player);
            }
        }
    </script>

        </div>

</div>


</body>
    """

    soup = BeautifulSoup(html_content, 'html.parser')

    # Initialize the QUESTIONS list
    QUESTIONS = []

    # Function to extract multiple-choice questions
    def extract_multiple_choice_questions(soup):
        questions_divs = soup.find_all('div', id=re.compile('multiple_choice-'))
        for div in questions_divs:
            # Extract the question title
            question_title_tag = div.find('p', class_='widget_title')
            if question_title_tag:
                question_title = question_title_tag.get_text(strip=True)
            else:
                continue  # Skip if no title

            # Extract the question text
            question_header = div.find('h5', class_='problem-description')
            if question_header:
                question_text = question_header.get_text(separator=' ', strip=True)
            else:
                continue  # Skip if no question text

            # Extract the options
            options = []
            form = div.find('form')
            if form:
                labels = form.find_all('label', class_='checkbox')
                for label in labels:
                    code_tag = label.find('code')
                    if code_tag:
                        option_text = code_tag.get_text(strip=True)
                        options.append(option_text)
                    else:
                        option_text = label.get_text(separator=' ', strip=True)
                        options.append(option_text)
                options_count = len(options)
                if options_count == 0:
                    continue  # Skip if no options
            else:
                continue  # Skip if no form

            # Create the question dictionary
            question_dict = {
                question_title: {
                    'question': question_text,
                    'options_count': options_count,
                    'options': options
                }
            }
            # Append to QUESTIONS list
            QUESTIONS.append(question_dict)

    # Function to extract coding questions
    def extract_coding_questions(soup):
        code_divs = soup.find_all('div', id=re.compile('python-'))
        for div in code_divs:
            # Extract the question title
            question_title_tag = div.find('p', class_='widget_title')
            if question_title_tag:
                question_title = question_title_tag.get_text(strip=True)
            else:
                continue  # Skip if no title

            # Extract the question text
            question_header = div.find('h5', class_='problem-description')
            if question_header:
                question_text = question_header.get_text(separator=' ', strip=True)
            else:
                continue  # Skip if no question text

            # Extract the code
            code_div = div.find('div', class_='CodeMirror-code')
            if code_div:
                code_lines = code_div.find_all('pre')
                code = '\n'.join([pre.get_text() for pre in code_lines])
            else:
                continue  # Skip if no code provided

            # Create the question dictionary
            question_dict = {
                question_title: [question_text, code]
            }
            # Append to QUESTIONS list
            QUESTIONS.append(question_dict)

    # Extract multiple-choice questions
    extract_multiple_choice_questions(soup)

    # Extract coding questions
    extract_coding_questions(soup)

    # Initialize the list to hold formatted question tuples
    formatted_questions = []

    # Process the QUESTIONS list and format each question into a single string
    for question in QUESTIONS:
        for title, content in question.items():
            question_str = f"Question Title: {title}\n"
            if isinstance(content, dict):  # Multiple-choice question
                question_str += f"Question:\n{content['question']}\n"
                question_str += f"Number of Options: {content['options_count']}\n"
                question_str += "Options:\n"
                for idx, option in enumerate(content['options'], 1):
                    question_str += f"{idx}. {option}\n"
                question_str += "Which one of these options is correct!"
            elif isinstance(content, list):  # Coding question
                question_str += f"Question:\n{content[0]}\n"
                question_str += "Code Provided:\n"
                question_str += f"{content[1]}\n"
                question_str += "Complete the code asked."
            # Add the formatted question string to the list along with the title
            formatted_questions.append((title, question_str))

    return formatted_questions

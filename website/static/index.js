// Code for markdown functionality from https://gist.github.com/ricardoalcocer/1acb94c3b53cd8ffa4a5
      window.onload=function(){
        // this function is the reverse version of escapeHTML found at 
        // https://github.com/evilstreak/markdown-js/blob/master/src/render_tree.js
        function unescapeHTML( text ) {
            return text.replace( /&amp;/g, "&" )
                       .replace( /&lt;/g, "<" )
                       .replace( /&gt;/g, ">" )
                       .replace( /&quot;/g, "\"" )
                       .replace( /&#39;/g, "'" );
          }

        // based on https://gist.github.com/paulirish/1343518
        (function(){

            [].forEach.call( document.querySelectorAll('[data-markdown]'), function fn(elem){
                showdown.setFlavor('github');
                elem.innerHTML = (new showdown.Converter({tables: true, strikethrough: true,ghCodeBlocks:true,emoji:true,tasklists:true,openLinksInNewWindow:true})).makeHtml(unescapeHTML(elem.innerHTML));
            });
        }());
    }

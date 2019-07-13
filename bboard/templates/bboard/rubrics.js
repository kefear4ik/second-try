var domain = 'kefear4ik.pythonanywhere.com/'

window.onload = function() {
    var list = document.getElementById('list');
    
    var rubricListLoader = new XMLHttpRequest()
    rubricListLoader.onreadystatechange = function() {
        if (rubricListLoader.readyState == 4) {
            if (rubricListLoader.status == 200) {
                var data = JSON.parse(rubricListLoader.responseText);
                var s = '<ul>';
                for (i=0; i < data.length; i++) {
                    s +='<li>' + data[i].name + '</li>';
                }
                s += '</ul>'
                list.innerHTML = s;
            }
        }
    }

    function rubricListLoad() {
        rubricListLoader.open('GET', domain + 'api/rubrics/', true);
        rubricListLoader.open();
    }

    rubricListLoad();
}
      

var domain = 'http://localhost:8000/'

window.onload = function() {
    var list = document.getElementById('list');
    
    var rubricListLoader = new XMLHttpRequest()
    rubricListLoader.onreadystatechange = function() {
        if (rubricListLoader.readyState == 4) {
            if (rubricListLoader.status == 200) {
                var data = JSON.parse(rubricListLoader.responseText);
                var s = '<ul>';
                for (i=0; i < data.length; i++) {
                    d = data[i];
                    detail_url = '<a href="' + domain +'api/rubrics/' +
                    d.id + '/" class="detail">Вывести</a>;
                    s +='<li>' + d.name + ' [' + detail_url + ']</li>';
                }
                s += '</ul>'
                list.innerHTML = s;
                links = list.querySelectorAll('ul li a.detail');
                for (var i = 0; i < links.length; i++) {
                    links[i].addEvenListener('click', rubricLoad);
                }
            }
        }
    }

    function rubricListLoad() {
        rubricListLoader.open('GET', domain + 'api/rubrics/', true);
        rubricListLoader.open();
    }

    rubricListLoad();
}
      

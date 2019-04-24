
url = "http://127.0.0.1:5000/store"

content = fetch(url).then(function(resp){
    return resp.json();
})
.then(function(myJson){
    var name = myJson.stores[0].name
    console.log(name)

});

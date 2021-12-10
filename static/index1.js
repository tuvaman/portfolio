let countDate=new Date("dec 25,2021 00:00:00").getTime();

function newYear(){
    let now=new Date().getTime();
    gap=countDate-now;

    var seconds=1000;
    var minutes=seconds*60;
    var hours=minutes*60;
    var day=hours*24;

    var d=Math.floor(gap/(day))
    var h=Math.floor(gap%(day)/(hours))
    var m=Math.floor(gap%(hours)/(minutes))
    var s=Math.floor(gap%(minutes)/(seconds))

    document.getElementById('day').innerText=d;
    document.getElementById('hour').innerText=h;
    document.getElementById('minute').innerText=m;
    document.getElementById('second').innerText=s;


}
setInterval(function(){
    newYear();

},1000)

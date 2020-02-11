let string = '';
function getButtonId (id){
  return id ;
}

function addToString(newStr, Str) {
  return Str.concat(newStr);
}

function getButton(id) {
  document.getElementById("box").value = string;
  if (getButtonId(id) == "="){
    ans = eval(string);
    alert(ans);
    string = ''
    return 0;
  }
  newStr = addToString(getButtonId(id), string);
  alert(newStr);
  string = newStr;
}
function turnToEssential (){
  string = document.getElementById("box").innerHTML ;
}

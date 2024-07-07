let screen= document.getElementById('screen');
buttons = document.querySelectorAll('button');
let string = '';
for(item of buttons){
    item.addEventListener('click', (e)=>{
        buttonText = e.target.innerText;
        console.log('Button :', buttonText)
        if(buttonText=='+'){
            buttonText = '+';
            string += buttonText;
            screen.value = string;
        }
        else if(buttonText=='-'){
            buttonText = '-';
            string += buttonText;
            screen.value = string;
        }
        else if(buttonText=='*'){
            buttonText = '*';
            string += buttonText;
            screen.value = string;
        }
        else if(buttonText=='/'){
            buttonText = '/';
            string += buttonText;
            screen.value = string;
        }
        else if(buttonText=='C'){
            string = "";
            screen.value = string;
        }
        else if(buttonText=='='){
            screen.value = eval(string);
        }
        else if(buttonText=='%'){
            buttonText = '%';
            string += buttonText;
            screen.value = string;
        }
        else if(buttonText=='00'){
            buttonText = '00';
            string += buttonText;
            screen.value = string;
        }
        else if(buttonText=='AC'){
            string = "";
            screen.value = string;
        }
        else if(buttonText=='DEL'){
            string = string.substring(0,string.length-1);
            screen.value = string;
        }
        else{
            string += buttonText;
            screen.value = string;
        }
    })
}
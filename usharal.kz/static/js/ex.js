// const transferClick = () => {
//     document.querySelectorAll(' .newCreatedButton').forEach(each => {
//         // console.log(each);
//         each.addEventListener('click', () => {
//             alert()
//             var parentFind = each.parentNode.parentNode.parentNode.classList[0];
//             var tin = document.querySelector(`.${parentFind} .chosenButton`).innerHTML
//             document.querySelector(`.${parentFind} .chosenButton`).classList.remove('chosenButton')
//             each.classList.add('chosenButton')
//             if(+each.innerHTML > +tin ){
//                 var a = (+each.innerHTML - +tin)*768
//                 $(`.${parentFind} .allMyContent`).animate({
//                     scrollTop: '+=' + a
//                 },1,'swing')
//             }
//             else{
//                 var a = (+tin - +each.innerHTML  )*768
//                 $(`.${parentFind} .allMyContent`).animate({
//                     scrollTop: '-=' + a
//                 },1,'swing')
//             }
//         })
//     })
// };

// // function sum(a,b){
// //     return a + b
// // }
// // export {sum};
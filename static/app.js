const formSubmitButton = document.getElementById('formSubmitButton');
const allCupcakesList = document.getElementById('allCupcakes');
const base_URL = 'http://127.0.0.1:5000'



async function getCupcakes(){
response = await axios.get(`${base_URL}/api/cupcakes`)

for(let cupcake of response.data.cupcakes){
  
  let newCupcake = document.createElement('div');
  newCupcake.setAttribute('id', 'cupCakeDiv')

  
  newCupcake.innerHTML=`
  <li data-cupcake-id=${cupcake.id}> 
  <b>${cupcake.flavor}</b> 
  <button class="delete-button"> X </button> 
  </li> 
    <ul> 
      <li> <b>size:</b>${cupcake.size}</li> 
      <li> <b>rating</b>:${cupcake.rating} </li>  
      <li> <img src=${cupcake.image} alt="no photo available"> </li> 
    </ul>`;


allCupcakesList.append(newCupcake)
}}



$(allCupcakesList).on("click", ".delete-button", async function (evt) {
  evt.preventDefault();
  let cupCakeDiv = document.getElementById('cupCakeDiv')
  let $cupcake = $(evt.target).closest("li");
  let cupcakeId = $cupcake.attr("data-cupcake-id");

  await axios.delete(`${base_URL}/api/cupcakes/${cupcakeId}`);

  cupCakeDiv.remove()

});

getCupcakes()


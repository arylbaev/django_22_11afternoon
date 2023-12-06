


const hello = () => console.log('hello world!')

//it's work
/*async function like(){
  //const datas = document.querySelector("#post_id")
  //let id = datas.dataset.postid;

  var post_id = document.getElementById('id_post')
  var id = post_id.getAttribute('post_id')

  let response = await fetch(`http://127.0.0.1:8000/line/api/post/${id}/like/`, {
    method: 'get',
    headers: {
      'X-Requested-With': 'XMLHttpRequest',
      'Content-Type': 'application/json'
    }
  })

  let data = await response.json()
  console.log(data)

  let p = document.getElementById('para')
  let text = document.createElement('text')
  text.innerHTML = await data
  p.appendChild(text)
}*/



async function makeRequest(url, method, body){
  let headers = {
      'X-Requested-With': 'XMLHttpRequest',
      'Content-Type': 'application/json'
    }

  if (method == 'post'){
    const csrf = document.querySelector('[name = csrfmiddlewaretoken]').value
    headers['X-CSRFToken'] = csrf
  }

  let response = await fetch(url, {
    method: method,
    headers: headers,
    body: body
  })

  return await response.json()
}

async function like(){
  var like_counter = document.getElementById('like_count').getAttribute('counter')
  var counter = like_counter
  //сделать здесь get или разбить лайк на like и unlike в views
  var post_info = document.getElementById('post_info')
  var post_id = post_info.getAttribute('post_id')
  var user_info = document.getElementById('user_info')
  var user_id = user_info.getAttribute('user_id')
  var url = `http://127.0.0.1:8000/line/api/post/${post_id}/like/`
  makeRequest(url, method='post', body=JSON.stringify({user_id: user_id, post_id: post_id}))


}
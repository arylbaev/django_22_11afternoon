


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

async function add_post(){
  console.log('comment')

    var comment_info = document.getElementById('comment_form')
    var comment = comment_info.value
    var post_info = document.getElementById('post_info')
    var post_id = post_info.getAttribute('post_id')
    var user_info = document.getElementById('user_info')
    var user_id = user_info.getAttribute('user_id')

    url = `http://127.0.0.1:8000/line/api/post/${post_id}/comment/`
    makeRequest(url, method='post', body=JSON.stringify({user_id: user_id, post_id: post_id, comment: comment}))

}
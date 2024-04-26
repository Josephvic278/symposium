function move_page(page_id){
    var get_page = document.querySelector(`div[page_id="${page_id}"]`)
    get_page.style.display = 'flex'
    get_page.style.transition = '1s'
    var page_line = document.querySelector(`div[line_id="${page_id}"]`)
    page_line.style.width ='100%'
    page_line.style.display = 'flex'
    page_line.style.transition = '0.5s'

    for (let i = 1; i <= 3; i++) {
        if (i!=page_id){
            other_pages = document.querySelector(`div[page_id="${i}"]`)
            other_pages.style.display = 'none'
            other_line = document.querySelector(`div[line_id="${i}"]`)
            other_line.style.width ='0%'
            other_line.style.transition = '0.5s'
        }
    }
}
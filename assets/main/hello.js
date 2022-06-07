$(".categories > a").on("click", function(){
    let a_href = $(this).attr("href")
    fetch(a_href + "?is_ajax=1").then(r => r.text()).then((data) => {
        window.history.pushState({}, "", a_href)
        $("#content").html(data)
    })
    return false
})

dubito find \
"SELECT si.id, si.price, si.sold, si.title, si.url, si.created_at, si.city, si.state, si.shipping_available, si.condition, slp.id as slp_id\
    FROM subito_query AS sq, subito_query_subito_list_page_through AS sqsl, subito_list_page AS slp, subito_insertion AS si
    WHERE (sq.id = sqsl.subitoquery_id AND sqsl.subitolistpage_id = slp.id AND slp.id = si.subito_list_page_id)
    
    AND sq.query = 'iphone 15'
    AND si.title LIKE '%iphone 15%'
    AND si.title NOT LIKE '%cover%'
    AND si.title NOT LIKE '%pellicol%'
    AND si.title NOT LIKE '%guscio%'
    AND si.title NOT LIKE '%custodi%'
    AND si.title NOT LIKE '%protettivo%'
    AND si.title NOT LIKE '%vetro temperato%'
    AND si.title NOT LIKE '%caricabatterie%'
    AND si.title NOT LIKE '%accessori%'
    AND si.title NOT LIKE '%cav%'
    AND si.title NOT LIKE '%proteggischermo%'
    AND si.title NOT LIKE '%protettore schermo%'
    AND si.title NOT LIKE '%vetro schermo%'
    AND si.title NOT LIKE '%magsafe%'
    AND si.title NOT LIKE '%display%'
    AND si.title NOT LIKE '%case%'
    AND si.price > 100

    ORDER BY si.price
" \
| dubito analyze "iphone 15" "iphone" "apple"

# --------------------------------------------

dubito find \
"SELECT si.id, si.price, si.sold, si.title, si.url, si.created_at, si.city, si.state, si.shipping_available, si.condition, slp.id as slp_id\
    FROM subito_query AS sq, subito_query_subito_list_page_through AS sqsl, subito_list_page AS slp, subito_insertion AS si
    WHERE (sq.id = sqsl.subitoquery_id AND sqsl.subitolistpage_id = slp.id AND slp.id = si.subito_list_page_id)
    
    AND sq.query = 'iphone 14'
    AND si.title LIKE '%iphone 14%'
    AND si.title NOT LIKE '%cover%'
    AND si.title NOT LIKE '%pellicol%'
    AND si.title NOT LIKE '%guscio%'
    AND si.title NOT LIKE '%custodi%'
    AND si.title NOT LIKE '%protettivo%'
    AND si.title NOT LIKE '%vetro temperato%'
    AND si.title NOT LIKE '%caricabatterie%'
    AND si.title NOT LIKE '%clone%'
    AND si.title NOT LIKE '%accessori%'
    AND si.title NOT LIKE '%cav%'
    AND si.title NOT LIKE '%ricambi%'
    AND si.title NOT LIKE '%progrip%'
    AND si.title NOT LIKE '%schermo%'
    AND si.title NOT LIKE '%rotto%'
    AND si.title NOT LIKE '%guasto%'
    AND si.title NOT LIKE '%scocca%'
    AND si.title NOT LIKE '%scheda madre%'
    AND si.title NOT LIKE '%proteggischermo%'
    AND si.title NOT LIKE '%protettore schermo%'
    AND si.title NOT LIKE '%vetro schermo%'
    AND si.title NOT LIKE '%magsafe%'
    AND si.title NOT LIKE '%display%'
    AND si.title NOT LIKE '%case%'
    AND si.price > 100
    AND si.price < 2000

    ORDER BY slp_id
" \
| dubito analyze "iphone 14" "iphone" "apple"

# --------------------------------------------

dubito find \
"SELECT si.id, si.price, si.sold, si.title, si.url, si.created_at, si.city, si.state, si.shipping_available, si.condition, slp.id as slp_id\
    FROM subito_query AS sq, subito_query_subito_list_page_through AS sqsl, subito_list_page AS slp, subito_insertion AS si
    WHERE (sq.id = sqsl.subitoquery_id AND sqsl.subitolistpage_id = slp.id AND slp.id = si.subito_list_page_id)
    
    AND sq.query = 'iphone 13'
    AND si.title LIKE '%iphone 13%'
    AND si.title NOT LIKE '%cover%'
    AND si.title NOT LIKE '%pellicol%'
    AND si.title NOT LIKE '%guscio%'
    AND si.title NOT LIKE '%custodi%'
    AND si.title NOT LIKE '%protettivo%'
    AND si.title NOT LIKE '%vetro temperato%'
    AND si.title NOT LIKE '%caricabatterie%'
    AND si.title NOT LIKE '%clone%'
    AND si.title NOT LIKE '%solo scatolo%'
    AND si.title NOT LIKE '%accessori%'
    AND si.title NOT LIKE '%da rimettere a posto%'
    AND si.title NOT LIKE '%cav%'
    AND si.title NOT LIKE '%ricambi%'
    AND si.title NOT LIKE '%progrip%'
    AND si.title NOT LIKE '%schermo%'
    AND si.title NOT LIKE '%rotto%'
    AND si.title NOT LIKE '%guasto%'
    AND si.title NOT LIKE '%scocca%'
    AND si.title NOT LIKE '%scheda madre%'
    AND si.title NOT LIKE '%proteggischermo%'
    AND si.title NOT LIKE '%protettore schermo%'
    AND si.title NOT LIKE '%c o m p r o%'
    AND si.title NOT LIKE '%vetro schermo%'
    AND si.title NOT LIKE '%magsafe%'
    AND si.title NOT LIKE '%display%'
    AND si.title NOT LIKE '%case%'
    AND si.price > 95
    AND si.price < 2000

    ORDER BY si.price
" \
| dubito analyze "iphone 13" "iphone" "apple"

# --------------------------------------------

dubito find \
"SELECT si.id, si.price, si.sold, si.title, si.url, si.created_at, si.city, si.state, si.shipping_available, si.condition, slp.id as slp_id\
    FROM subito_query AS sq, subito_query_subito_list_page_through AS sqsl, subito_list_page AS slp, subito_insertion AS si
    WHERE (sq.id = sqsl.subitoquery_id AND sqsl.subitolistpage_id = slp.id AND slp.id = si.subito_list_page_id)
    
    AND sq.query = 'iphone 12'
    AND si.title LIKE '%iphone 12%'
    AND si.title NOT LIKE '%cover%'
    AND si.title NOT LIKE '%pellicol%'
    AND si.title NOT LIKE '%guscio%'
    AND si.title NOT LIKE '%custodi%'
    AND si.title NOT LIKE '%protettivo%'
    AND si.title NOT LIKE '%vetro temperato%'
    AND si.title NOT LIKE '%caricabatterie%'
    AND si.title NOT LIKE '%clone%'
    AND si.title NOT LIKE '%quad lock moto%'
    AND si.title NOT LIKE '%camera posteriore%'
    AND si.title NOT LIKE '%fotocamera%'
    AND si.title NOT LIKE '%solo scatolo%'
    AND si.title NOT LIKE '%accessori%'
    AND si.title NOT LIKE '%da rimettere a posto%'
    AND si.title NOT LIKE '%filtri sandmarc%'
    AND si.title NOT LIKE '%cav%'
    AND si.title NOT LIKE '%ricambi%'
    AND si.title NOT LIKE '%progrip%'
    AND si.title NOT LIKE '%schermo%'
    AND si.title NOT LIKE '%rotto%'
    AND si.title NOT LIKE '%guasto%'
    AND si.title NOT LIKE '%scocca%'
    AND si.title NOT LIKE '%scheda madre%'
    AND si.title NOT LIKE '%proteggischermo%'
    AND si.title NOT LIKE '%protettore schermo%'
    AND si.title NOT LIKE '%c o m p r o%'
    AND si.title NOT LIKE '%vetro schermo%'
    AND si.title NOT LIKE '%magsafe%'
    AND si.title NOT LIKE '%display%'
    AND si.title NOT LIKE '%case%'
    AND si.price > 50
    AND si.price < 1280

    ORDER BY si.price
" \
| dubito analyze "iphone 12" "iphone" "apple"

# --------------------------------------------

dubito find \
"SELECT si.id, si.price, si.sold, si.title, si.url, si.created_at, si.city, si.state, si.shipping_available, si.condition, slp.id as slp_id\
    FROM subito_query AS sq, subito_query_subito_list_page_through AS sqsl, subito_list_page AS slp, subito_insertion AS si
    WHERE (sq.id = sqsl.subitoquery_id AND sqsl.subitolistpage_id = slp.id AND slp.id = si.subito_list_page_id)
    
    AND sq.query = 'iphone 11'
    AND si.title LIKE '%iphone 11%'
    AND si.title NOT LIKE '%cover%'
    AND si.title NOT LIKE '%pellicol%'
    AND si.title NOT LIKE '%guscio%'
    AND si.title NOT LIKE '%custodi%'
    AND si.title NOT LIKE '%protettivo%'
    AND si.title NOT LIKE '%vetro temperato%'
    AND si.title NOT LIKE '%caricabatterie%'
    AND si.title NOT LIKE '%clone%'
    AND si.title NOT LIKE '%quad lock%'
    AND si.title NOT LIKE '%quadlock%'
    AND si.title NOT LIKE '%camera posteriore%'
    AND si.title NOT LIKE '%fotocamer%'
    AND si.title NOT LIKE '%solo scatolo%'
    AND si.title NOT LIKE '%accessori%'
    AND si.title NOT LIKE '%da rimettere a posto%'
    AND si.title NOT LIKE '%filtri sandmarc%'
    AND si.title NOT LIKE '%cav%'
    AND si.title NOT LIKE '%ricambi%'
    AND si.title NOT LIKE '%non funzionante%'
    AND si.title NOT LIKE '%progrip%'
    AND si.title NOT LIKE '%6.1%'
    AND si.title NOT LIKE '%schermo%'
    AND si.title NOT LIKE '%rotto%'
    AND si.title NOT LIKE '%guasto%'
    AND si.title NOT LIKE '%scocca%'
    AND si.title NOT LIKE '%scheda madre%'
    AND si.title NOT LIKE '%proteggischermo%'
    AND si.title NOT LIKE '%protettore schermo%'
    AND si.title NOT LIKE '%c o m p r o%'
    AND si.title NOT LIKE '%vetro schermo%'
    AND si.title NOT LIKE '%magsafe%'
    AND si.title NOT LIKE '%display%'
    AND si.title NOT LIKE '%case%'
    AND si.title NOT LIKE '%twitter%'
    AND si.title NOT LIKE '%apple watch%'
    AND si.title NOT LIKE '%ipad%'
    AND si.price > 80
    AND si.price < 1200

    ORDER BY si.price
" \
| dubito analyze "iphone 11" "iphone" "apple"

# --------------------------------------------

dubito find \
"SELECT si.id, si.price, si.sold, si.title, si.url, si.created_at, si.city, si.state, si.shipping_available, si.condition, slp.id as slp_id\
    FROM subito_query AS sq, subito_query_subito_list_page_through AS sqsl, subito_list_page AS slp, subito_insertion AS si
    WHERE (sq.id = sqsl.subitoquery_id AND sqsl.subitolistpage_id = slp.id AND slp.id = si.subito_list_page_id)
    
    AND (sq.query = 'iphone 10' OR sq.query = 'iphone x')
    AND (si.title LIKE '%iphone 10%' OR si.title LIKE '%iphone x%')
    AND si.title NOT LIKE '%cover%'
    AND si.title NOT LIKE '%pellicol%'
    AND si.title NOT LIKE '%guscio%'
    AND si.title NOT LIKE '%custodi%'
    AND si.title NOT LIKE '%protettivo%'
    AND si.title NOT LIKE '%vetro temperato%'
    AND si.title NOT LIKE '%caricabatterie%'
    AND si.title NOT LIKE '%clone%'
    AND si.title NOT LIKE '%quad lock%'
    AND si.title NOT LIKE '%quadlock%'
    AND si.title NOT LIKE '%camera posteriore%'
    AND si.title NOT LIKE '%fotocamer%'
    AND si.title NOT LIKE '%solo scatolo%'
    AND si.title NOT LIKE '%accessori%'
    AND si.title NOT LIKE '%da rimettere a posto%'
    AND si.title NOT LIKE '%filtri sandmarc%'
    AND si.title NOT LIKE '%cav%'
    AND si.title NOT LIKE '%ricambi%'
    AND si.title NOT LIKE '%non funzionante%'
    AND si.title NOT LIKE '%progrip%'
    AND si.title NOT LIKE '%6.1%' 
    AND si.title NOT LIKE '%schermo%'
    AND si.title NOT LIKE '%rotto%'
    AND si.title NOT LIKE '%guasto%'
    AND si.title NOT LIKE '%scocca%'
    AND si.title NOT LIKE '%scheda madre%'
    AND si.title NOT LIKE '%proteggischermo%'
    AND si.title NOT LIKE '%protettore schermo%'
    AND si.title NOT LIKE '%c o m p r o%'
    AND si.title NOT LIKE '%vetro schermo%'
    AND si.title NOT LIKE '%magsafe%'
    AND si.title NOT LIKE '%display%'
    AND si.title NOT LIKE '%case%'
    AND si.title NOT LIKE '%twitter%'
    AND si.price > 60
    AND si.price < 1280

    ORDER BY si.price
" \
| dubito analyze "iphone 10" "iphone" "apple"

# --------------------------------------------

dubito find \
"SELECT si.id, si.price, si.sold, si.title, si.url, si.created_at, si.city, si.state, si.shipping_available, si.condition, slp.id as slp_id\
    FROM subito_query AS sq, subito_query_subito_list_page_through AS sqsl, subito_list_page AS slp, subito_insertion AS si
    WHERE (sq.id = sqsl.subitoquery_id AND sqsl.subitolistpage_id = slp.id AND slp.id = si.subito_list_page_id)
    
    AND sq.query = 'iphone 8'
    AND si.title LIKE '%iphone 8%'
    AND si.title NOT LIKE '%cover%'
    AND si.title NOT LIKE '%pellicol%'
    AND si.title NOT LIKE '%guscio%'
    AND si.title NOT LIKE '%custodi%'
    AND si.title NOT LIKE '%protettivo%'
    AND si.title NOT LIKE '%vetro temperato%'
    AND si.title NOT LIKE '%caricabatterie%'
    AND si.title NOT LIKE '%clone%'
    AND si.title NOT LIKE '%quad lock%'
    AND si.title NOT LIKE '%quadlock%'
    AND si.title NOT LIKE '%camera posteriore%'
    AND si.title NOT LIKE '%fotocamer%'
    AND si.title NOT LIKE '%solo scatolo%'
    AND si.title NOT LIKE '%accessori%'
    AND si.title NOT LIKE '%da rimettere a posto%'
    AND si.title NOT LIKE '%filtri sandmarc%'
    AND si.title NOT LIKE '%cav%'
    AND si.title NOT LIKE '%ricambi%'
    AND si.title NOT LIKE '%non funzionante%'
    AND si.title NOT LIKE '%progrip%'
    AND si.title NOT LIKE '%6.1%' 
    AND si.title NOT LIKE '%schermo%'
    AND si.title NOT LIKE '%rotto%'
    AND si.title NOT LIKE '%guasto%'
    AND si.title NOT LIKE '%scocca%'
    AND si.title NOT LIKE '%scheda madre%'
    AND si.title NOT LIKE '%proteggischermo%'
    AND si.title NOT LIKE '%protettore schermo%'
    AND si.title NOT LIKE '%c o m p r o%'
    AND si.title NOT LIKE '%vetro schermo%'
    AND si.title NOT LIKE '%magsafe%'
    AND si.title NOT LIKE '%display%'
    AND si.title NOT LIKE '%case%'
    AND si.title NOT LIKE '%twitter%'
    AND si.title NOT LIKE '%omaggio%'
    AND si.title NOT LIKE '%iphone 12%'
    AND si.title NOT LIKE '%plus%'
    AND si.price > 30

    ORDER BY si.price
" \
| dubito analyze "iphone 8" "iphone" "apple"

# --------------------------------------------

dubito find \
"SELECT si.id, si.price, si.sold, si.title, si.url, si.created_at, si.city, si.state, si.shipping_available, si.condition, slp.id as slp_id\
    FROM subito_query AS sq, subito_query_subito_list_page_through AS sqsl, subito_list_page AS slp, subito_insertion AS si
    WHERE (sq.id = sqsl.subitoquery_id AND sqsl.subitolistpage_id = slp.id AND slp.id = si.subito_list_page_id)
    
    AND sq.query = 'iphone 7'
    AND si.title LIKE '%iphone 7%'
    AND si.title NOT LIKE '%cover%'
    AND si.title NOT LIKE '%pellicol%'
    AND si.title NOT LIKE '%guscio%'
    AND si.title NOT LIKE '%custodi%'
    AND si.title NOT LIKE '%protettivo%'
    AND si.title NOT LIKE '%vetro temperato%'
    AND si.title NOT LIKE '%caricabatterie%'
    AND si.title NOT LIKE '%clone%'
    AND si.title NOT LIKE '%quad lock%'
    AND si.title NOT LIKE '%quadlock%'
    AND si.title NOT LIKE '%camera posteriore%'
    AND si.title NOT LIKE '%fotocamer%'
    AND si.title NOT LIKE '%solo scatolo%'
    AND si.title NOT LIKE '%accessori%'
    AND si.title NOT LIKE '%da rimettere a posto%'
    AND si.title NOT LIKE '%filtri sandmarc%'
    AND si.title NOT LIKE '%cav%'
    AND si.title NOT LIKE '%ricambi%'
    AND si.title NOT LIKE '%non funzionante%'
    AND si.title NOT LIKE '%progrip%'
    AND si.title NOT LIKE '%6.1%' 
    AND si.title NOT LIKE '%schermo%'
    AND si.title NOT LIKE '%rotto%'
    AND si.title NOT LIKE '%guasto%'
    AND si.title NOT LIKE '%scocca%'
    AND si.title NOT LIKE '%scheda madre%'
    AND si.title NOT LIKE '%proteggischermo%'
    AND si.title NOT LIKE '%protettore schermo%'
    AND si.title NOT LIKE '%c o m p r o%'
    AND si.title NOT LIKE '%vetro schermo%'
    AND si.title NOT LIKE '%magsafe%'
    AND si.title NOT LIKE '%display%'
    AND si.title NOT LIKE '%case%'
    AND si.title NOT LIKE '%twitter%'
    AND si.price > 15
    AND si.price < 400

    ORDER BY si.price
" \
| dubito analyze "iphone 7" "iphone" "apple"

# --------------------------------------------

dubito find \
"SELECT si.id, si.price, si.sold, si.title, si.url, si.created_at, si.city, si.state, si.shipping_available, si.condition, slp.id as slp_id\
    FROM subito_query AS sq, subito_query_subito_list_page_through AS sqsl, subito_list_page AS slp, subito_insertion AS si
    WHERE (sq.id = sqsl.subitoquery_id AND sqsl.subitolistpage_id = slp.id AND slp.id = si.subito_list_page_id)
    
    AND sq.query = 'iphone 6'
    AND si.title LIKE '%iphone 6%'
    AND si.title NOT LIKE '%cover%'
    AND si.title NOT LIKE '%pellicol%'
    AND si.title NOT LIKE '%guscio%'
    AND si.title NOT LIKE '%custodi%'
    AND si.title NOT LIKE '%protettivo%'
    AND si.title NOT LIKE '%vetro temperato%'
    AND si.title NOT LIKE '%caricabatterie%'
    AND si.title NOT LIKE '%clone%'
    AND si.title NOT LIKE '%quad lock%'
    AND si.title NOT LIKE '%quadlock%'
    AND si.title NOT LIKE '%camera posteriore%'
    AND si.title NOT LIKE '%fotocamer%'
    AND si.title NOT LIKE '%solo scatolo%'
    AND si.title NOT LIKE '%accessori%'
    AND si.title NOT LIKE '%da rimettere a posto%'
    AND si.title NOT LIKE '%filtri sandmarc%'
    AND si.title NOT LIKE '%cav%'
    AND si.title NOT LIKE '%ricambi%'
    AND si.title NOT LIKE '%non funzionante%'
    AND si.title NOT LIKE '%progrip%'
    AND si.title NOT LIKE '%6.1%' 
    AND si.title NOT LIKE '%schermo%'
    AND si.title NOT LIKE '%rotto%'
    AND si.title NOT LIKE '%guasto%'
    AND si.title NOT LIKE '%scocca%'
    AND si.title NOT LIKE '%scheda madre%'
    AND si.title NOT LIKE '%proteggischermo%'
    AND si.title NOT LIKE '%protettore schermo%'
    AND si.title NOT LIKE '%c o m p r o%'
    AND si.title NOT LIKE '%vetro schermo%'
    AND si.title NOT LIKE '%magsafe%'
    AND si.title NOT LIKE '%display%'
    AND si.title NOT LIKE '%case%'
    AND si.title NOT LIKE '%twitter%'
    AND si.price > 15
    AND si.price < 400

    ORDER BY si.price
" \
| dubito analyze "iphone 6" "iphone" "apple"

# --------------------------------------------

dubito find \
"SELECT si.id, si.price, si.sold, si.title, si.url, si.created_at, si.city, si.state, si.shipping_available, si.condition, slp.id as slp_id\
    FROM subito_query AS sq, subito_query_subito_list_page_through AS sqsl, subito_list_page AS slp, subito_insertion AS si
    WHERE (sq.id = sqsl.subitoquery_id AND sqsl.subitolistpage_id = slp.id AND slp.id = si.subito_list_page_id)
    
    AND sq.query = 'iphone 5'
    AND si.title LIKE '%iphone 5%'
    AND si.title NOT LIKE '%cover%'
    AND si.title NOT LIKE '%pellicol%'
    AND si.title NOT LIKE '%guscio%'
    AND si.title NOT LIKE '%custodi%'
    AND si.title NOT LIKE '%protettivo%'
    AND si.title NOT LIKE '%vetro temperato%'
    AND si.title NOT LIKE '%caricabatterie%'
    AND si.title NOT LIKE '%clone%'
    AND si.title NOT LIKE '%quad lock%'
    AND si.title NOT LIKE '%quadlock%'
    AND si.title NOT LIKE '%camera posteriore%'
    AND si.title NOT LIKE '%fotocamer%'
    AND si.title NOT LIKE '%solo scatolo%'
    AND si.title NOT LIKE '%accessori%'
    AND si.title NOT LIKE '%da rimettere a posto%'
    AND si.title NOT LIKE '%filtri sandmarc%'
    AND si.title NOT LIKE '%cav%'
    AND si.title NOT LIKE '%ricambi%'
    AND si.title NOT LIKE '%non funzionante%'
    AND si.title NOT LIKE '%progrip%'
    AND si.title NOT LIKE '%6.1%' 
    AND si.title NOT LIKE '%schermo%'
    AND si.title NOT LIKE '%rotto%'
    AND si.title NOT LIKE '%guasto%'
    AND si.title NOT LIKE '%scocca%'
    AND si.title NOT LIKE '%scheda madre%'
    AND si.title NOT LIKE '%proteggischermo%'
    AND si.title NOT LIKE '%protettore schermo%'
    AND si.title NOT LIKE '%c o m p r o%'
    AND si.title NOT LIKE '%vetro schermo%'
    AND si.title NOT LIKE '%magsafe%'
    AND si.title NOT LIKE '%display%'
    AND si.title NOT LIKE '%case%'
    AND si.title NOT LIKE '%twitter%'
    AND si.price > 15

    ORDER BY si.price
" \
| dubito analyze "iphone 5" "iphone" "apple"

# --------------------------------------------

dubito find \
"SELECT si.id, si.price, si.sold, si.title, si.url, si.created_at, si.city, si.state, si.shipping_available, si.condition, slp.id as slp_id\
    FROM subito_query AS sq, subito_query_subito_list_page_through AS sqsl, subito_list_page AS slp, subito_insertion AS si
    WHERE (sq.id = sqsl.subitoquery_id AND sqsl.subitolistpage_id = slp.id AND slp.id = si.subito_list_page_id)
    
    AND sq.query = 'iphone 4'
    AND si.title LIKE '%iphone 4%'
    AND si.title NOT LIKE '%cover%'
    AND si.title NOT LIKE '%pellicol%'
    AND si.title NOT LIKE '%guscio%'
    AND si.title NOT LIKE '%custodi%'
    AND si.title NOT LIKE '%protettivo%'
    AND si.title NOT LIKE '%vetro temperato%'
    AND si.title NOT LIKE '%caricabatterie%'
    AND si.title NOT LIKE '%clone%'
    AND si.title NOT LIKE '%quad lock%'
    AND si.title NOT LIKE '%quadlock%'
    AND si.title NOT LIKE '%camera posteriore%'
    AND si.title NOT LIKE '%fotocamer%'
    AND si.title NOT LIKE '%solo scatolo%'
    AND si.title NOT LIKE '%accessori%'
    AND si.title NOT LIKE '%cuffie%'
    AND si.title NOT LIKE '%da rimettere a posto%'
    AND si.title NOT LIKE '%filtri sandmarc%'
    AND si.title NOT LIKE '%cav%'
    AND si.title NOT LIKE '%ricambi%'
    AND si.title NOT LIKE '%non funzionante%'
    AND si.title NOT LIKE '%progrip%'
    AND si.title NOT LIKE '%6.1%' 
    AND si.title NOT LIKE '%schermo%'
    AND si.title NOT LIKE '%rotto%'
    AND si.title NOT LIKE '%guasto%'
    AND si.title NOT LIKE '%scocca%'
    AND si.title NOT LIKE '%scheda madre%'
    AND si.title NOT LIKE '%proteggischermo%'
    AND si.title NOT LIKE '%protettore schermo%'
    AND si.title NOT LIKE '%c o m p r o%'
    AND si.title NOT LIKE '%stand%'
    AND si.title NOT LIKE '%scatola%'
    AND si.title NOT LIKE '%vetro schermo%'
    AND si.title NOT LIKE '%magsafe%'
    AND si.title NOT LIKE '%display%'
    AND si.title NOT LIKE '%case%'
    AND si.title NOT LIKE '%twitter%'
    AND si.title NOT LIKE '%iphone 5%'
    AND si.price > 10
    AND si.price < 400

    ORDER BY si.price
" \
| dubito analyze "iphone 4" "iphone" "apple"

# --------------------------------------------

dubito find \
"SELECT si.id, si.price, si.sold, si.title, si.url, si.created_at, si.city, si.state, si.shipping_available, si.condition, slp.id as slp_id\
    FROM subito_query AS sq, subito_query_subito_list_page_through AS sqsl, subito_list_page AS slp, subito_insertion AS si
    WHERE (sq.id = sqsl.subitoquery_id AND sqsl.subitolistpage_id = slp.id AND slp.id = si.subito_list_page_id)
    
    AND sq.query = 'iphone 3'
    AND si.title LIKE '%iphone 3%'
    AND si.title NOT LIKE '%cover%'
    AND si.title NOT LIKE '%pellicol%'
    AND si.title NOT LIKE '%guscio%'
    AND si.title NOT LIKE '%custodi%'
    AND si.title NOT LIKE '%protettivo%'
    AND si.title NOT LIKE '%vetro temperato%'
    AND si.title NOT LIKE '%caricabatterie%'
    AND si.title NOT LIKE '%clone%'
    AND si.title NOT LIKE '%quad lock%'
    AND si.title NOT LIKE '%quadlock%'
    AND si.title NOT LIKE '%camera posteriore%'
    AND si.title NOT LIKE '%fotocamer%'
    AND si.title NOT LIKE '%solo scatolo%'
    AND si.title NOT LIKE '%accessori%'
    AND si.title NOT LIKE '%cuffie%'
    AND si.title NOT LIKE '%da rimettere a posto%'
    AND si.title NOT LIKE '%filtri sandmarc%'
    AND si.title NOT LIKE '%cav%'
    AND si.title NOT LIKE '%ricambi%'
    AND si.title NOT LIKE '%non funzionante%'
    AND si.title NOT LIKE '%progrip%'
    AND si.title NOT LIKE '%6.1%' 
    AND si.title NOT LIKE '%schermo%'
    AND si.title NOT LIKE '%rotto%'
    AND si.title NOT LIKE '%guasto%'
    AND si.title NOT LIKE '%scocca%'
    AND si.title NOT LIKE '%scheda madre%'
    AND si.title NOT LIKE '%proteggischermo%'
    AND si.title NOT LIKE '%protettore schermo%'
    AND si.title NOT LIKE '%c o m p r o%'
    AND si.title NOT LIKE '%stand%'
    AND si.title NOT LIKE '%scatola%'
    AND si.title NOT LIKE '%vetro schermo%'
    AND si.title NOT LIKE '%magsafe%'
    AND si.title NOT LIKE '%display%'
    AND si.title NOT LIKE '%case%'
    AND si.title NOT LIKE '%twitter%'
    AND si.title NOT LIKE '%iphone 5%'
    AND si.title NOT LIKE '%supporto%'
    AND si.title NOT LIKE '%dock%'
    AND si.title NOT LIKE '%radio%'
    AND si.title NOT LIKE '%caricatore%'
    AND si.title NOT LIKE '%carica%'
    AND si.price > 10
    AND si.price < 400

    ORDER BY si.price
" \
| dubito analyze "iphone 3" "iphone" "apple"

# --------------------------------------------

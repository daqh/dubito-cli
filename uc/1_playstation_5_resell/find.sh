dubito find \
"SELECT si.id, si.price, si.sold, si.title, si.url, si.created_at, si.city, si.state, si.shipping_available, si.condition, slp.id as slp_id\
    FROM subito_query AS sq, subito_query_subito_list_page_through AS sqsl, subito_list_page AS slp, subito_insertion AS si
    WHERE (sq.id = sqsl.subitoquery_id AND sqsl.subitolistpage_id = slp.id AND slp.id = si.subito_list_page_id)
    
    AND (sq.query LIKE '%playstation 5%' OR sq.query LIKE '%ps5%')
    AND (si.title LIKE '%playstation 5%' OR si.title LIKE '%ps5%')
    AND si.title NOT LIKE '%bundle%'
    AND si.title NOT LIKE '%vr%'
    AND si.title NOT LIKE '%portal%'
    AND si.description NOT LIKE '%portal%'
    AND si.description NOT LIKE '%vr%'
    AND si.description NOT LIKE '%accessori%'
    AND si.title NOT LIKE '%fifa%'
    AND si.title NOT LIKE '%stick%'
    AND si.title NOT LIKE '%collector%'
    AND si.title NOT LIKE '%riparazione%'
    AND si.title NOT LIKE '%cuffie%'
    AND si.title NOT LIKE '%pc%'
    AND si.title NOT LIKE '%monitor%'
    AND si.title NOT LIKE '%C£RCO%'
    AND si.title NOT LIKE '%volante%'
    AND si.title NOT LIKE '%giochi%'
    AND si.title NOT LIKE '%cerc0%'
    AND si.title NOT LIKE '%difettosa%'
    AND si.title NOT LIKE '%C.E.R.C.O%'
    AND si.description NOT LIKE '%fifa%'
    AND si.price > 200

    ORDER BY si.price
" \
| dubito analyze "playstation 5" "playstation" "sony"

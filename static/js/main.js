$(document).ready(function(){
    $.getJSON('static/data/buildings.json', function(buildings){

        
        var names = Object.keys(buildings);

        $.each(names, function(i, name){
            
            // buildings_wrap = $('<div/>').addClass('building-wrap').appendTo($('#buildings'));
            buildings_wrap = $('<table/>').addClass('building-wrap').appendTo($('#buildings'));

            // $('<div/>').addClass('building-name').attr('colspan', 5).text(name).appendTo(buildings_wrap)
            $('<th/>').addClass('building-name').attr('colspan', 5).text(name).appendTo(buildings_wrap)
            // name

            $.each(buildings[name], function(j, entry){

                // building_wrap = $('<div/>').addClass('building-entry').appendTo(buildings_wrap);
                building_wrap = $('<tr/>').addClass('building-entry').appendTo(buildings_wrap);

                $('<td/>').addClass('building-property').text(entry.lv).appendTo(building_wrap);
                $('<td/>').addClass('building-property').text(entry.cost).appendTo(building_wrap);
                $('<td/>').addClass('building-property').text(entry.time).appendTo(building_wrap);
                $('<td/>').addClass('building-property').text(entry.time_str).appendTo(building_wrap);
                $('<td/>').addClass('building-property').text(entry.type).appendTo(building_wrap);   

                // $('<div/>').addClass('building-property').text(entry.lv).appendTo(building_wrap);
                // $('<div/>').addClass('building-property').text(entry.cost).appendTo(building_wrap);
                // $('<div/>').addClass('building-property').text(entry.time).appendTo(building_wrap);
                // $('<div/>').addClass('building-property').text(entry.time_str).appendTo(building_wrap);
                // $('<div/>').addClass('building-property').text(entry.type).appendTo(building_wrap);                
            });
        });
    });
});

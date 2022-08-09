var mapContainer = document.getElementById('map');
		var mapOption = {
			center: new kakao.maps.LatLng(37.58631, 127.02936),
			level: 4
		}

		var map = new kakao.maps.Map(mapContainer, mapOption);

		/* DB 정보 저장 */
		const buildings = "{{buildings}}";
		const temp1 = JSON.parse(buildings.replace(/(&quot\;)/g,"\""));

        const facilities = "{{facilities}}";
        const temp2 = JSON.parse(facilities.replace(/(&quot\;)/g,"\""));
		// view에서 받아온 DB담아두기 

		/* Building 중심 >> 위도, 경도 좌표 저장 */
		const buildingLocations  = temp1.map(element => {return  {
			pk: element.pk,
        	latlng: new kakao.maps.LatLng(element.fields.building_lat, element.fields.building_lon),
          lat: element.fields.building_lat,
          long: element.fields.building_lon,
		  history: element.fields.history,
        }} );

		// console.log(temp1)
        // console.log(temp2)
        /* Facility 중심 >> 위도, 경도 좌표 저장 */
        const facilityLocations = temp2.map(element => {return {
            category: element.fields.category,
            facility_loc: element.fields.facility_loc,
            facility_name: element.fields.facility_name,
            building_id: element.fields.building_id
        }

        })
        // console.log(buildingLocations)
        // console.log(facilityLocations)

		/* 카테고리별 객체 담아두기 */

        //공부중이라서 메모 . . .
		// let cafe = facilityLocations.filter((element)=> {return element['category'] == 'cafe'});
		// let lounge = facilityLocations.filter((element)=> {return element['category'] == 'lounge'});
		// let book = facilityLocations.filter((element)=> {return element['category'] == 'book_return'});
        
		// console.log(cafe);
		// console.log(lounge);
		// console.log(book);

        /* 카테고리별 좌표 저장 */
        // const cafeLocation = cafe.filter((element)=> {return })
        // const loungeLocation = new Object()
        // const bookLocation = new Object()
        let cafe = []
        let lounge = []
        let book = []

        facilityLocations.forEach(function(item, index, arr){
            if (item['category'] == 'cafe'){
                cafe.push(item['building_id'])
            }
            else if (item['category'] == 'lounge'){
                lounge.push(item['building_id'])
            }
            else if (item['category'] == 'book_return'){
                book.push(item['building_id'])
            }
        }
        )
        
        cafe = Array.from(new Set(cafe))
        lounge = Array.from(new Set(lounge))
        book = Array.from(new Set(book))

        // 각 카테고리별 마커들이 표시될 좌표배열
        let cafeLocation = []
        let loungeLocation = []
        let bookLocation = []
        
        // pk값이랑 building_id헷갈림
        // pk값은 builiding_id보다 1이 더 큼 (building_id는 배열 index라서 0부터 시작하지만, pk는 1부터 시작)
        buildingLocations.forEach(function(item, index, arr){
            cafe.forEach((k) => {
                if (item['pk'] == k)
                cafeLocation.push(item['latlng'])
            })
        
          
            lounge.forEach((k) => {
                if (item['pk'] == k)
                loungeLocation.push(item['latlng'])
            })

            book.forEach((k) => {
                if (item['pk'] == k)
                bookLocation.push(item['latlng'])
            })
        }
        )
        console.log(cafeLocation)
        console.log(loungeLocation)
        console.log(bookLocation)
        

        var markerImageSrc = 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/category.png';  // 마커이미지의 주소입니다. 스프라이트 이미지 입니다
            cafeMarkers = [], // 카페 마커 객체를 가지고 있을 배열입니다
            loungeMarkers = [], // 라운지 (아직은 편의점) 마커 객체를 가지고 있을 배열입니다
            bookMarkers = []; // 책자동반납기 (아직은 주차장) 마커 객체를 가지고 있을 배열입니다

        
        createCafeMarkers(); // 카페 마커를 생성하고 커피숍 마커 배열에 추가합니다
        createLoungeMarkers(); // 라운지 마커를 생성하고 편의점 마커 배열에 추가합니다
        createBookMarkers(); // 책자동반납기 마커를 생성하고 주차장 마커 배열에 추가합니다

        // console.log(cafeLocation)
        // console.log(loungeLocation)
        // console.log(bookLocation)

        changeMarker('lounge'); // 지도에 커피숍 마커가 보이도록 설정합니다 
        
        // 마커이미지의 주소와, 크기, 옵션으로 마커 이미지를 생성하여 리턴하는 함수입니다
        function createMarkerImage(src, size, options) {
            var markerImage = new kakao.maps.MarkerImage(src, size, options);
            return markerImage;            
        }
        
        // 좌표와 마커이미지를 받아 마커를 생성하여 리턴하는 함수입니다
        function createMarker(position, image) {
            var marker = new kakao.maps.Marker({
                position: position,
                image: image
            });
    
            return marker;  
        }
        
        /* -------------- 카페 ----------------*/
        // 카페 마커를 생성하고 커피숍 마커 배열에 추가하는 함수입니다
        function createCafeMarkers() {
            
            for (var i = 0; i < cafeLocation.length; i++) {  
                
                var imageSize = new kakao.maps.Size(22, 26),
                    imageOptions = {  
                        spriteOrigin: new kakao.maps.Point(10, 0),    
                        spriteSize: new kakao.maps.Size(36, 98)  
                    };     
                
                // 마커이미지와 마커를 생성합니다
                var markerImage = createMarkerImage(markerImageSrc, imageSize, imageOptions),    
                    marker = createMarker(cafeLocation[i], markerImage);  
                
                // 생성된 마커를 카페 마커 배열에 추가합니다
                cafeMarkers.push(marker);
            }     
        }

        // 카페 마커들의 지도 표시 여부를 설정하는 함수입니다
        function setCafeMarkers(map) {        
            for (var i = 0; i < cafeMarkers.length; i++) {  
                cafeMarkers[i].setMap(map);
            }        
        }

        /* -------------- 라운지 ----------------*/
        // 라운지 마커를 생성하고 라운지 마커 배열에 추가하는 함수입니다
        function createLoungeMarkers() {
            
            for (var i = 0; i < loungeLocation.length; i++) {  
                
                var imageSize = new kakao.maps.Size(22, 26),
                    imageOptions = {  
                        spriteOrigin: new kakao.maps.Point(10, 36),    
                        spriteSize: new kakao.maps.Size(36, 98)  
                    };     
                
                // 마커이미지와 마커를 생성합니다
                var markerImage = createMarkerImage(markerImageSrc, imageSize, imageOptions),    
                    marker = createMarker(loungeLocation[i], markerImage);  
                
                // 생성된 마커를 라운지 마커 배열에 추가합니다
                loungeMarkers.push(marker);
            }     
        }

        // 라운지 마커들의 지도 표시 여부를 설정하는 함수입니다
        function setLoungeMarkers(map) {        
            for (var i = 0; i < loungeMarkers.length; i++) {  
                loungeMarkers[i].setMap(map);
            }        
        }

        /* -------------- 책 ----------------*/
        // 책 마커를 생성하고 책 마커 배열에 추가하는 함수입니다
        function createBookMarkers() {
            
            for (var i = 0; i < bookLocation.length; i++) {  
                
                var imageSize = new kakao.maps.Size(22, 26),
                    imageOptions = {  
                        spriteOrigin: new kakao.maps.Point(10, 72),    
                        spriteSize: new kakao.maps.Size(36, 98)  
                    };     
                
                // 마커이미지와 마커를 생성합니다
                var markerImage = createMarkerImage(markerImageSrc, imageSize, imageOptions),    
                    marker = createMarker(bookLocation[i], markerImage);  
                
                // 생성된 마커를 책 마커 배열에 추가합니다
                bookMarkers.push(marker);
            }     
        }

        // 책 마커들의 지도 표시 여부를 설정하는 함수입니다
        function setBookMarkers(map) {        
            for (var i = 0; i < bookMarkers.length; i++) {  
                bookMarkers[i].setMap(map);
            }        
        }

        // 카테고리를 클릭했을 때 type에 따라 카테고리의 스타일과 지도에 표시되는 마커를 변경합니다
        function changeMarker(type){
            
            var cafeMenu = document.getElementById('cafeMenu');
            var loungeMenu = document.getElementById('loungeMenu');
            var bookMenu = document.getElementById('bookMenu');
            
            // 커피숍 카테고리가 클릭됐을 때
            if (type === 'cafe') {
            
                // 커피숍 카테고리를 선택된 스타일로 변경하고
                cafeMenu.className = 'menu_selected';
                
                // 편의점과 주차장 카테고리는 선택되지 않은 스타일로 바꿉니다
                loungeMenu.className = '';
                bookMenu.className = '';
                
                // 커피숍 마커들만 지도에 표시하도록 설정합니다
                setCafeMarkers(map);
                setLoungeMarkers(null);
                setBookMarkers(null);
                
            } else if (type === 'lounge') { // 편의점 카테고리가 클릭됐을 때
            
                // 편의점 카테고리를 선택된 스타일로 변경하고
                cafeMenu.className = '';
                loungeMenu.className = 'menu_selected';
                bookMenu.className = '';
                
                // 편의점 마커들만 지도에 표시하도록 설정합니다
                setCafeMarkers(null);
                setLoungeMarkers(map);
                setBookMarkers(null);
                
            } else if (type === 'book') { // 주차장 카테고리가 클릭됐을 때
            
                // 주차장 카테고리를 선택된 스타일로 변경하고
                cafeMenu.className = '';
                loungeMenu.className = '';
                bookMenu.className = 'menu_selected';
                
                // 주차장 마커들만 지도에 표시하도록 설정합니다
                setCafeMarkers(null);
                setLoungeMarkers(null);
                setBookMarkers(map);  
            }    
        } 
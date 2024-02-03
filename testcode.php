<?php
/* Template Name: Office Search */

$user_id = get_current_user_id();
$selected_size = (isset($_GET['size']) && !empty($_GET['size'])) ? $_GET['size'] : '';
$selected_desks = (isset($_GET['desks']) && !empty($_GET['desks'])) ? $_GET['desks'] : '';
$selected_sort_by = (isset($_GET['sort-by']) && !empty($_GET['sort-by'])) ? $_GET['sort-by'] : '';
$lat = (isset($_GET['lat']) && !empty($_GET['lat'])) ? $_GET['lat'] : '';
$lng = (isset($_GET['lng']) && !empty($_GET['lng'])) ? $_GET['lng'] : '';
$search = ((isset($_GET['search'])) ? $_GET['search'] : '');
$size_property = array('50-500'=>'1-15','500-1000'=>'15-40','1000-2500'=>'40-100','2500-5000'=>'100-200','5000'=>'200');
$desks_property = array('1-15'=>'50-500','15-40'=>'500-1000','40-100'=>'1000-2500','100-200'=>'2500-5000','200'=>'5000');
if($selected_size !=''){
	$selected_desks = $size_property[$selected_size];
}
if($selected_desks !=''){
	$selected_size = $desks_property[$selected_desks];
}
?>
	<div class="search-row d-flex flex-wrap">
		<form name="property-filter" id="property_filter" method="GET" class="property-filter">
		<div class="search-input">
			<input type="search" name="search" id="pac-input" placeholder="Search Location" value="<?php echo $search; ?>">
			<input type="hidden" name="lat" value="<?php echo $lat; ?>">
			<input type="hidden" name="lng" value="<?php echo $lng; ?>">
			<button type="submit">
				<svg xmlns="http://www.w3.org/2000/svg" width="23.161" height="23.161" viewBox="0 0 23.161 23.161">
				  <path id="iconmonstr-magnifier-6" d="M20.432,23.161,13.3,16.032A8.706,8.706,0,1,1,16.032,13.3l7.129,7.129-2.729,2.729ZM8.685,15.441A6.755,6.755,0,1,0,1.93,8.685,6.763,6.763,0,0,0,8.685,15.441Z" fill="#603cdb"></path>
				</svg>
			</button>
		</div>
		<div class="btn-group-row d-flex">
			<div class="col-space dropdown-col">
				<select name="size" class="size-property" id="size_property">
					<option value="">Size Sq. Ft.</option>
					<option value="50-500" <?php selected($selected_size,'50-500'); ?>>50-500 Sq. Ft.</option>
					<option value="500-1000" <?php selected($selected_size,'500-1000'); ?>>500-1000 Sq. Ft.</option>
					<option value="1000-2500" <?php selected($selected_size,'1000-2500'); ?>>1000-2500 Sq. Ft.</option>
					<option value="2500-5000" <?php selected($selected_size,'2500-5000'); ?>>2500-5000 Sq. Ft.</option>
					<option value="5000" <?php selected($selected_size,'5000'); ?>>5000+ Sq. Ft.</option>
				</select>
			</div>
			<div class="col-space dropdown-col">
				<select name="desks" class="desks-property" id="desks_property">
					<option value="">Desks</option>
					<option value="1-15" <?php selected($selected_desks,'1-15'); ?>>1-15 Desks</option>
					<option value="15-40" <?php selected($selected_desks,'15-40'); ?>>15-40 Desks</option>
					<option value="40-100" <?php selected($selected_desks,'40-100'); ?>>40-100 Desks</option>
					<option value="100-200" <?php selected($selected_desks,'100-200'); ?>>100-200 Desks</option>
					<option value="200" <?php selected($selected_desks,'200'); ?>>200+ Desks</option>
				</select>
			</div><?php
			$clicked = 'true';
			if(isset($_GET['scroll']) && $_GET['scroll'] == 'false')
			{
				$clicked = 'false';
			} ?>
			<input type="hidden" name="scroll" value="<?php echo $clicked;?>">
			<div class="col-space border-btn filter-btn">
				<a href="javascript:void(0)">
					<svg xmlns="http://www.w3.org/2000/svg" width="17.084" height="18" viewBox="0 0 17.084 18">
					  <path id="iconmonstr-filter-1" d="M1,0H18.084L11.1,11.321V18L7.989,15.75V11.321Z" transform="translate(-1)" fill="#603cdb"/>
					</svg>
					<span>Filters</span>
				</a>
			</div>
			<div class="col-space sortBy-dropdown dropdown-col">
				<span class="icon">
					<svg xmlns="http://www.w3.org/2000/svg" width="24" height="18" viewBox="0 0 24 18">
					  <path id="iconmonstr-sort-25" d="M6,3,0,11H4V21H8V11h4ZM22,17H14V15h8Zm2,2H14v2H24Zm-4-8H14v2h6ZM18,7H14V9h4ZM16,3H14V5h2Z" transform="translate(0 -3)" fill="#603cdb"/>
					</svg>
				</span>
				<select name="sort-by" class="sort-by" id="sort_by">
					<option value="">Sort By</option>
					<option value="desc" <?php selected($selected_sort_by,'desc'); ?>>Recently added</option>
					<option value="hightolow" <?php selected($selected_sort_by,'hightolow'); ?>>Price high to low</option>
					<option value="lowtohigh" <?php selected($selected_sort_by,'lowtohigh'); ?>>Price low to high</option>
				</select>
			</div>
<!-- 		</form> -->
			<div class="col-space border-btn shortlist-btn">
				<a href="javascript:void(0)" id="view_shortlist">
					<svg xmlns="http://www.w3.org/2000/svg" width="20.637" height="19.204" viewBox="0 0 20.637 19.204">
					  <path id="iconmonstr-favorite-4" d="M5.138,2.636c2.648,0,4.069,2.856,4.68,4.116.614-1.266,2.02-4.108,4.685-4.108A3.319,3.319,0,0,1,18,6.066C18,8.882,14.119,12.49,9.818,16.7c-4.3-4.214-8.182-7.821-8.182-10.636a3.312,3.312,0,0,1,3.5-3.43ZM5.139,1A4.945,4.945,0,0,0,0,6.066C0,9.88,4.557,13.779,9.818,19c5.261-5.221,9.818-9.12,9.818-12.934A4.933,4.933,0,0,0,14.5,1.008,5.346,5.346,0,0,0,9.818,3.657,5.339,5.339,0,0,0,5.139,1Z" transform="translate(0.5 -0.5)" fill="#603cdb" stroke="#603cdb" stroke-width="1"/>
					</svg>
					<span>View Shortlist</span>
				</a>
			</div>
			<div class="col-space border-btn hide-map-btn">
				<a href="javascript:void(0)">
					<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18">
					  <path id="iconmonstr-map-8_1_" data-name="iconmonstr-map-8 (1)" d="M9,0A4.474,4.474,0,0,0,4.5,4.277C4.5,7.788,8.087,8.159,9,13.5c.913-5.341,4.5-5.712,4.5-9.223A4.473,4.473,0,0,0,9,0ZM9,6a1.5,1.5,0,1,1,1.5-1.5A1.5,1.5,0,0,1,9,6Zm9,12-5.03-1.82L9,18,4.814,16.18,0,18l3-6.75,2.97-1.188a8.533,8.533,0,0,1,.8,1.3L4.123,12.416,2.83,15.326l2-.758,1.129-2.015-.476,2.283,3.142,1.342L9,14.663l.349,1.518,3.112-1.418L12,12.488l1.179,2.172,2.049.742-1.3-2.983-2.686-1.061a8.4,8.4,0,0,1,.8-1.3l3.016,1.191Z" fill="#603cdb"/>
					</svg>
					<span>Hide map</span>
				</a>
			</div>
		</div>
	</div>
	<!-- Filter modal -->
	<div class="filterModal-main">
		<div class="filterMiddle">
			<div class="filterModal-main-wrap">
				<div class="close-btn">
					<a href="javascript:void(0)">Close</a>
				</div>
				<div class="modal-title">Filter by</div>
				<form class="form">
					<div class="modal-wrap d-flex flex-wrap">
						<div class="modal-col location-col">
							<div class="col-title">Location</div>
							<div class="col-data"><?php
								$locations = get_terms( array(
								    'taxonomy' => 'location',
								    'hide_empty' => false,
								));								
								$count_terms = round(count($locations) / 2);
								$location_ids = (isset($_GET['location_ids'])) ? $_GET['location_ids'] : '';
								if($location_ids)
								{
									$location_ids = explode(',', $location_ids);
								}?>
								<div class="modal-checkbox-group d-flex flex-wrap">
									<div class="col50"><?php
									$x=0;
									foreach( $locations as $location ) {
										$checked_location = '';
										if($x!=0 && $x%$count_terms==0){ 
                      echo '</div><div class="col50">';
                    }
                    if(!empty($location_ids) && in_array($location->term_id,$location_ids))
                    {
                    	$checked_location = 'checked';
                    }
                    echo '<div class="modal-checkbox">
											<input type="checkbox" name="location_ids" '.$checked_location.' id="'.$location->slug.'" value="'.$location->term_id.'">
											<label for="'.$location->slug.'">'.$location->name.'</label>
										</div>';
										++$x;
									}?>
									</div>									
								</div>
								<div class="bottom-btn-group d-flex flex-wrap small-screen">
									<button type="submit" class="btn submit-filter">Apply</button>
									<button type="button" class="reset-btn">Clear</button>
								</div>
							</div>
						</div>
						<div class="modal-col size-col">
							<div class="col-title">Size Sq. Ft.</div>
							<div class="col-data">
								<div class="modal-radio-group d-flex flex-wrap">
									<div class="col100">
										<div class="modal-radio">
											<input type="radio" name="size" id="50-500" value="50-500" <?php checked($selected_size,'50-500'); ?>>
											<label for="50-500">50-500</label>
										</div>
										<div class="modal-radio">
											<input type="radio" name="size" id="500-1000" value="500-1000" <?php checked($selected_size,'500-1000'); ?>>
											<label for="500-1000">500-1000</label>
										</div>
										<div class="modal-radio">
											<input type="radio" name="size" id="1000-2500" value="1000-2500" <?php checked($selected_size,'1000-2500'); ?>>
											<label for="1000-2500">1000-2500</label>
										</div>
										<div class="modal-radio">
											<input type="radio" name="size" id="2500-5000" value="2500-5000" <?php checked($selected_size,'2500-5000'); ?>>
											<label for="2500-5000">2500-5000</label>
										</div>
										<div class="modal-radio">
											<input type="radio" name="size" id="5000+" value="5000" <?php checked($selected_size,'5000'); ?>>
											<label for="5000+">5000+</label>
										</div>
									</div>
								</div>
								<div class="bottom-btn-group d-flex flex-wrap small-screen">
									<button type="submit" class="btn submit-filter">Apply</button>
									<button type="button" class="reset-btn">Clear</button>
								</div>
							</div>
						</div>							
						<div class="modal-col desks-col">
							<div class="col-title">Desks</div>
							<div class="col-data">
								<div class="modal-radio-group d-flex flex-wrap">
									<div class="col100">
										<div class="modal-radio">
											<input type="radio" name="desks" id="1-15" value="1-15" <?php checked($selected_desks,'1-15'); ?>>
											<label for="1-15">1-15</label>
										</div>
										<div class="modal-radio">
											<input type="radio" name="desks" id="15-40" value="15-40" <?php checked($selected_desks,'15-40'); ?>>
											<label for="15-40">15-40</label>
										</div>
										<div class="modal-radio">
											<input type="radio" name="desks" id="40-100" value="40-100" <?php checked($selected_desks,'40-100'); ?>>
											<label for="40-100">40-100</label>
										</div>
										<div class="modal-radio">
											<input type="radio" name="desks" id="100-200" value="100-200" <?php checked($selected_desks,'100-200'); ?>>
											<label for="100-200">100-200</label>
										</div>
										<div class="modal-radio">
											<input type="radio" name="desks" id="200+" value="200" <?php checked($selected_desks,'200'); ?>>
											<label for="200+">200+</label>
										</div>
									</div>
								</div>
								<div class="bottom-btn-group d-flex flex-wrap small-screen"><?php
									$clicked = 'true';
									if(isset($_GET['scroll']) && $_GET['scroll'] == 'false')
									{
										$clicked = 'false';
									} ?>
									<input type="hidden" name="scroll" value="<?php echo $clicked;?>">
									<button type="submit" class="btn submit-filter">Apply</button>
									<button type="button" class="reset-btn">Clear</button>
								</div>
							</div>
						</div> <?php
						$amenities = get_terms(array('taxonomy' => 'amenities','hide_empty' => false));
						$amenitiesn_ids = array();
						if(isset($_GET['amenitiesn_ids'])) {
							$amenitiesn_ids = explode(',', $_GET['amenitiesn_ids']);
						}
						if($amenities) {
							$count_ame_terms = round(count($amenities) / 4);
						?>
						<div class="modal-col amenities-col">
							<div class="col-title">Amenities</div>
							<div class="col-data">
								<div class="modal-checkbox-group d-flex flex-wrap">
									<div class="col25"><?php
									$x=0;
									foreach( $amenities as $amenitie ) {
										$checked_amenitiesn = '';
										if($x!=0 && $x%$count_ame_terms==0){ 
                      echo '</div><div class="col25">';
                    }
                    if(in_array($amenitie->term_id,$amenitiesn_ids))
                    {
                    	$checked_amenitiesn = 'checked';
                    }
                    echo '<div class="modal-checkbox">
												<input type="checkbox" name="amenitiesn_ids" '.$checked_amenitiesn.' id="'.$amenitie->slug.'" value="'.$amenitie->term_id.'">
												<label for="'.$amenitie->slug.'">'.$amenitie->name.'</label>
										</div>';
										++$x;
									}?>
									</div>
								</div>
								<div class="bottom-btn-group d-flex flex-wrap small-screen">
									<button type="submit" class="btn submit-filter">Apply</button>
									<button type="button" class="reset-btn">Clear</button>
								</div>
							</div>
						</div> <?php
						} ?>
					</div>
					<div class="bottom-btn-group d-flex flex-wrap large-screen hide-small-screen">
						<button type="submit" class="btn submit-filter">Submit</button>
						<a href="<?php echo home_url('/office-search/');?>" class="reset-btn">Reset All</a>
					</div>
				</form>
			</div>
		</div>
	</div>
	<?php
  $pagenum = ((isset($_GET['pagenum'])) ? $_GET['pagenum'] : 1);
	$location_ids = ((isset($_GET['location_ids'])) ? $_GET['location_ids'] : '');
	$amenitiesn_ids = ((isset($_GET['amenitiesn_ids'])) ? $_GET['amenitiesn_ids'] : '');
  $posts_per_page = -1;
  $args_property = get_office_search_query($selected_size,$selected_sort_by,$pagenum,$location_ids,$amenitiesn_ids,$search,$posts_per_page,$lat,$lng);
	$the_query = new WP_Query($args_property);
	$count_posts = $the_query->found_posts;	?>
<?php
$private_office_prices = array(); // Initialize the array outside the loop

while ($the_query->have_posts()): $the_query->the_post();
    // Get private office details
    $private_offices = get_field('private_office');

    // Check if private office details are available and get the price of the first private office
    if (!empty($private_offices)) {
        $first_private_office = $private_offices[0];
        $price = $first_private_office['price'];
        $cleaned_price = preg_replace('/\D/', '', $price);
        $private_office_prices[] = (int) $cleaned_price; // Save cleaned price in the array
    }
endwhile;
?>

<!-- Output the JavaScript array after the loop -->
<script type="text/javascript">
    const privatePrices = <?php echo json_encode($private_office_prices); ?>;
</script>

<!-- Your existing JavaScript code that uses the privatePrices array -->
<script type="text/javascript">
    const drc_propertis = <?php drc_get_all_properties($the_query);?>;

    // Loop through properties to update and display cleaned prices
    for (let i = 0; i < drc_propertis.length; i++) {
        const property = drc_propertis[i];

        // Use the first private office price for the property
        const cleaned_price = privatePrices[i];
        const formatted_price = Number(cleaned_price).toLocaleString();

        // Update the property_price with cleaned and formatted price
        property.property_price = formatted_price;
    }

    // Now you can use the updated property data to display on the screen
//     console.log(drc_propertis); // Display the updated property data
</script>

<!-- 	<script type="text/javascript">
		const drc_propertis = <?php drc_get_all_properties($the_query);?>;
	</script> -->
	<div class="search-wrap">
		<input type="hidden" value="<?php echo $count_posts; ?>" id="count_property">
		<div class="search-result d-flex flex-wrap">
			<div class="left-col">
				<div class="result-tottle"></div>
				<div class="inside sb-container map-record">
						<div class="account_slider d-flex flex-wrap map-record"></div>
						<div class="col-sm-12 text-center pagi_num">									
							<ul class="list-cptapagination"></ul>
						</div>
				</div>
			</div>
			<div class="map-right"><?php
				$clicked = 'clicked';
				if(isset($_GET['scroll']) && $_GET['scroll'] == 'false')
				{
					$clicked = '';
				} ?>
				<a href="javascript:void(0);" class="move-btn <?php echo $clicked; ?>">Search as I move the map</a>
				<div class="map-main">
					<div class="map" id="map"></div>
				</div>
			</div>
		</div>
		<div class="cta-block-row">
			<div class="cta-block-small">
				<div class="inside">
					<div class="bg-img">
						<img src="<?php echo get_field('background_image','option');?>" alt="">
					</div>
					<div class="text-block text-center">						
						<h2><?php echo get_field('request_a_call_back_heading','option');?></h2>
						<div class="bottom-btn">
							<a href="javascript:void(0)" class="request-modal-btn btn"><?php echo get_field('request_callback_title','option');?></a>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>

<div class="shortlist-modal-box">
	<div class="small-screen modal-close-btn"></div>
	<div class="top-part">
	</div>
	<div class="bottom-part">
		<div class="btn-div">
			<a href="#" class="btn email-my-shortlist">Email my shortlist</a>
		</div>
		<div class="btn-div">
			<a href="javascript:void(0)" class="request-modal-btn btn"><?php echo get_field('request_callback_title','option');?></a>
		</div>
		<div class="call-us">
			<span><?php echo get_field('call_us_heading','option');?></span>
			<a href="tel:+020 7183 8458"><?php echo get_field('call_us_number','option');?></a>
		</div>
	</div>
</div>
<script type="text/javascript">
	jQuery(function(){
	  jQuery('input[type="radio"][name="size"]').change(function(e){
	  	jQuery('input[type="radio"][name="desks"][value="'+size_property[this.value]+'"]').prop('checked', true);
	  		jQuery('input[name="pfs"]').val('size');
		});
	  jQuery('input[type="radio"][name="desks"]').change(function(e){
	  	jQuery('input[type="radio"][name="size"][value="'+desks_property[this.value]+'"]').prop('checked', true);
	  		jQuery('input[name="pfs"]').val('desks');
		});
	});
</script>

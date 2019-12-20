// frappe.ready(function() {
// 	// bind events here
// })

// function hideShow() {
// 	$('input[data-fieldname="total_amount"]').val('')
// 	$('input[data-fieldname="total_advance"]').val('')
// 	$('input[data-fieldname="total_balance"]').val('')
// 	$('[data-fieldname=couple], [data-fieldname=kids], [data-fieldname=male_stag], [data-fieldname=female_stag], [data-fieldname=people]').val('')
// 	let party = $('select[data-fieldname=booking_for]')[0].value
// 	if(party === 'Sunset Party on 30th December') {
// 		$('[data-fieldname=couple], [data-fieldname=kids], [data-fieldname=male_stag], [data-fieldname=female_stag]').hide()
// 		$('[data-fieldname=people]').show()
// 		$('[for=couple], [for=kids], [for=male_stag], [for=female_stag], [for=table]').hide()
// 		$('[for=people]').show()
// 		$('select[data-fieldname=table]').hide()
// 		$('[for=pay_advance]').hide()
// 		$('[data-fieldname=pay_advance]').hide()
// 	} else {
// 		$('[data-fieldname=couple], [data-fieldname=kids], [data-fieldname=male_stag], [data-fieldname=female_stag]').show()
// 		$('[data-fieldname=people]').hide()
// 		$('[for=couple], [for=kids], [for=male_stag], [for=female_stag], [for=table]').show()
// 		$('[for=people]').hide()
// 		$('select[data-fieldname=table]').show()
// 		$('[for=pay_advance]').show()
// 		$('[data-fieldname=pay_advance]').show()

// 	}
// }
// hideShow()

// $('[data-fieldname=coupon]').on('input', function(){
// 	totalAmount()
// })

// function totalAmount() {
// 	let total
// 	let advance_total
// 	var party = $('select[data-fieldname=booking_for]')[0].value
// 	if(party === 'Sunset Party on 30th December'){
// 		total = $('select[data-fieldname="people"]')[0].value * 500
// 	} else {
// 		total = $('select[data-fieldname="kids"]')[0].value*500 + $('select[data-fieldname="couple"]')[0].value*3000+ $('select[data-fieldname="female_stag"]')[0].value*1000 + $('select[data-fieldname="male_stag"]')[0].value*2000
// 	}
// 	let coupon = $('[data-fieldname=coupon]')[0].value
// 	if(coupon.toLowerCase() === 'bop') {
// 		total = total - .05*total
// 	}
// 	if(coupon.toLowerCase() === 'pula') {
// 		total = total - .15*total
// 	} 
// 	if(coupon.toLowerCase() === '10off') {
//                 total = total - .10*total
//         }
// 	if(coupon.toLowerCase() === 'jugaad') {
// 		total = total - .2*total
// 	}

// 	if($('select[data-fieldname=table]')[0].value == 'Yes' && party != "Sunset Party on 30th December") {
// 		total = total + .5 * total
// 	}

// 	let advance = $('[data-fieldname=pay_advance]')[0].value
// 	if(advance == '20%'){
// 		advance_total = 0.2*total
// 	}
// 	if(advance == '50%'){
// 		advance_total = 0.5*total
// 	}
// 	if(advance == '100%'){
// 		advance_total = total
// 	}

// 	advance_total = (party === 'Sunset Party on 30th December') ? total : advance_total
// 	$('input[data-fieldname="total_amount"]').val(total)
// 	$('input[data-fieldname="total_advance"]').val(advance_total)
// 	$('input[data-fieldname="total_balance"]').val(total - advance_total)

// 	//return total
// }

// $('select[data-fieldname=booking_for]').on('change', function(){
// 	$('select[data-fieldname=table]')[0].value = "No"
// 	hideShow()
// })

// $('[data-fieldname=table], [data-fieldname=couple], [data-fieldname=people], [data-fieldname=kids], [data-fieldname=female_stag], [data-fieldname=male_stag], [data-fieldname=pay_advance]').on('change', function(){
// 	totalAmount()
// 	if($('select[data-fieldname=table]')[0].value == 'Yes'){
// 		let party = $('select[data-fieldname=booking_for]')[0].value
// 		let text = (party != "Sunset Party on 30th December") ? "Total " + $('[data-fieldname=pay_advance]')[0].value + " Advance (Table Guaranteed)" : "Total (Table Guaranteed)"
// 		$('[for=total_amount]')[0].innerText = text
// 	} else {
// 		let party = $('select[data-fieldname=booking_for]')[0].value
// 		let text = (party != "Sunset Party on 30th December") ? "Total " + $('[data-fieldname=pay_advance]')[0].value + " Advance (Table First come first serve)" : "Total (Table first come first serve)"
// 		$('[for=total_amount]')[0].innerText = text
// 	}
// })

frappe.web_form.on('name1', (field, name) => {
	alert('ggg')
})

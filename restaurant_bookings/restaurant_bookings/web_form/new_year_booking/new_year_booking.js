frappe.ready(function() {
	// bind events here
})

function hideShow() {
	$('input[name="total_amount"]').val('')
	$('input[name="total_advance"]').val('')
	$('input[name="total_balance"]').val('')
	$('[name=couple], [name=kids], [name=male_stag], [name=female_stag], [name=people]').val('')
	let party = $('select[name=booking_for]')[0].value
	if(party === 'Sunset Party on 30th December') {
		$('[name=couple], [name=kids], [name=male_stag], [name=female_stag]').hide()
		$('[name=people]').show()
		$('[for=couple], [for=kids], [for=male_stag], [for=female_stag], [for=table]').hide()
		$('[for=people]').show()
		$('select[name=table]').hide()
		$('[for=pay_advance]').hide()
		$('[name=pay_advance]').hide()
	} else {
		$('[name=couple], [name=kids], [name=male_stag], [name=female_stag]').show()
		$('[name=people]').hide()
		$('[for=couple], [for=kids], [for=male_stag], [for=female_stag], [for=table]').show()
		$('[for=people]').hide()
		$('select[name=table]').show()
		$('[for=pay_advance]').show()
		$('[name=pay_advance]').show()

	}
}
hideShow()

$('[name=coupon]').on('input', function(){
	totalAmount()
})

function totalAmount() {
	let total
	let advance_total
	var party = $('select[name=booking_for]')[0].value
	if(party === 'Sunset Party on 30th December'){
		total = $('select[name="people"]')[0].value * 500
	} else {
		total = $('select[name="kids"]')[0].value*500 + $('select[name="couple"]')[0].value*3000+ $('select[name="female_stag"]')[0].value*1000 + $('select[name="male_stag"]')[0].value*2000
	}
	let coupon = $('[name=coupon]')[0].value
	if(coupon.toLowerCase() === 'bop') {
		total = total - .05*total
	}
	if(coupon.toLowerCase() === 'pula') {
		total = total - .15*total
	} 
	if(coupon.toLowerCase() === '10off') {
                total = total - .10*total
        }
	if(coupon.toLowerCase() === 'jugaad') {
		total = total - .2*total
	}

	if($('select[name=table]')[0].value == 'Yes' && party != "Sunset Party on 30th December") {
		total = total + .5 * total
	}

	let advance = $('[name=pay_advance]')[0].value
	if(advance == '20%'){
		advance_total = 0.2*total
	}
	if(advance == '50%'){
		advance_total = 0.5*total
	}
	if(advance == '100%'){
		advance_total = total
	}

	advance_total = (party === 'Sunset Party on 30th December') ? total : advance_total
	$('input[name="total_amount"]').val(total)
	$('input[name="total_advance"]').val(advance_total)
	$('input[name="total_balance"]').val(total - advance_total)

	//return total
}

$('select[name=booking_for]').on('change', function(){
	$('select[name=table]')[0].value = "No"
	hideShow()
})

$('[name=table], [name=couple], [name=people], [name=kids], [name=female_stag], [name=male_stag], [name=pay_advance]').on('change', function(){
	totalAmount()
	if($('select[name=table]')[0].value == 'Yes'){
		let party = $('select[name=booking_for]')[0].value
		let text = (party != "Sunset Party on 30th December") ? "Total " + $('[name=pay_advance]')[0].value + " Advance (Table Guaranteed)" : "Total (Table Guaranteed)"
		$('[for=total_amount]')[0].innerText = text
	} else {
		let party = $('select[name=booking_for]')[0].value
		let text = (party != "Sunset Party on 30th December") ? "Total " + $('[name=pay_advance]')[0].value + " Advance (Table First come first serve)" : "Total (Table first come first serve)"
		$('[for=total_amount]')[0].innerText = text
	}
})

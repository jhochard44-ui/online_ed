capture log close
clear all
set more off

* ELK valuation model in Stata
* ---------------------------------------------
* This do-file recreates the pricing valuation logic from the API service layer
* so valuation can be run fully in Stata.
*
* Required variables in memory:
*   - rate_per_hour      : expert hourly rate
*   - duration_minutes   : session duration (minutes)
*   - group_size         : number of attendees
*   - group_discount     : multiplier applied for group sessions (e.g. 0.85)
*
* Output variable:
*   - elk_valuation      : final quoted price

capture program drop elk_valuation_model
program define elk_valuation_model
    version 17.0
    syntax

    confirm variable rate_per_hour
    confirm variable duration_minutes
    confirm variable group_size
    confirm variable group_discount

    tempvar hours base_price
    gen double `hours' = duration_minutes / 60
    gen double `base_price' = rate_per_hour * `hours'

    gen double elk_valuation = round(`base_price', 0.01)
    replace elk_valuation = round(`base_price' * group_discount, 0.01) if group_size > 1

    label var elk_valuation "ELK valuation (session quote)"
end

* Example run (remove/replace with your own import if needed)
input double rate_per_hour int duration_minutes byte group_size double group_discount
120 60 1 0.85
120 90 2 0.85
175 45 3 0.80
end

elk_valuation_model
list, noobs abbreviate(20)

package main

import (
    "fmt"
    "time"
)

var (
    ARIES      = time.Date(2019, time.Month(3), 21, 0, 0, 0, 0, time.UTC)
    TAURUS     = time.Date(2019, time.Month(4), 21, 0, 0, 0, 0, time.UTC)
    GEMINI     = time.Date(2019, time.Month(5), 21, 0, 0, 0, 0, time.UTC)
    CANCER     = time.Date(2019, time.Month(6), 22, 0, 0, 0, 0, time.UTC)
    LEO        = time.Date(2019, time.Month(7), 23, 0, 0, 0, 0, time.UTC)
    VIRGO      = time.Date(2019, time.Month(8), 23, 0, 0, 0, 0, time.UTC)
    LIBRA      = time.Date(2019, time.Month(9), 22, 0, 0, 0, 0, time.UTC)
    SCORPIO    = time.Date(2019, time.Month(10), 23, 0, 0, 0, 0, time.UTC)
    SAGITAURUS = time.Date(2019, time.Month(11), 23, 0, 0, 0, 0, time.UTC)
    CAPRICORN  = time.Date(2019, time.Month(12), 22, 0, 0, 0, 0, time.UTC)
    AQUARIUS   = time.Date(2020, time.Month(1), 21, 0, 0, 0, 0, time.UTC)
    PISCES     = time.Date(2020, time.Month(2), 20, 0, 0, 0, 0, time.UTC)
)

func compDate(start, end, check time.Time) bool {
    sday := start.Day() - 1
    eday := end.Day()
    mStart := time.Date(start.Year(), start.Month(), sday, 0, 0, 0, 0, time.UTC)
    mEnd := time.Date(end.Year(), end.Month(), eday, 0, 0, 0, 0, time.UTC)
    return check.After(mStart) && check.Before(mEnd)
}

func getAstro(dt time.Time) string {
    var result string
    if compDate(ARIES, TAURUS, dt) {
        result = "Aries"
    } else if compDate(TAURUS, GEMINI, dt) {
        result = "Taurus"
    } else if compDate(GEMINI, CANCER, dt) {
        result = "Gemini"
    } else if compDate(CANCER, LEO, dt) {
        result = "Cancer"
    } else if compDate(LEO, VIRGO, dt) {
        result = "Leo"
    } else if compDate(VIRGO, LIBRA, dt) {
        result = "Virgo"
    } else if compDate(LIBRA, SCORPIO, dt) {
        result = "Libra"
    } else if compDate(SCORPIO, SAGITAURUS, dt) {
        result = "Scorpio"
    } else if compDate(SAGITAURUS, CAPRICORN, dt) {
        result = "Sagittarius"
    } else if compDate(CAPRICORN, AQUARIUS, dt) {
        result = "Capricorn"
    } else if compDate(AQUARIUS, PISCES, dt) {
        result = "Aquarius"
    } else {
        result = "Pisces"
    }
    return result
}

func convertMonth(strMonth string) int {
    var result int
    switch strMonth {
    case "Jan":
        result = 1
    case "Feb":
        result = 2
    case "Mar":
        result = 3
    case "Apr":
        result = 4
    case "May":
        result = 5
    case "Jun":
        result = 6
    case "Jul":
        result = 7
    case "Aug":
        result = 8
    case "Sep":
        result = 9
    case "Oct":
        result = 10
    case "Nov":
        result = 11
    case "Dec":
        result = 12
    }
    return result
}

func getYear(month, day int) int {
    if month == 3 && day < 21 {
        return 2020
    } else if month <= 2 {
        return 2020
    } else {
        return 2019
    }
}

func main() {
    var number int
    fmt.Scanln(&number)
    result := []string{}
    for i := 0; i < number; i++ {
        var day int
        var month string
        fmt.Scanf("%d %s\n", &day, &month)
        mon := convertMonth(month)
        year := getYear(mon, day)
        dt := time.Date(year, time.Month(mon), day, 00, 00, 00, 00, time.UTC)
        result = append(result, getAstro(dt))
    }

    for _, val := range result {
        fmt.Println(val)
    }

}

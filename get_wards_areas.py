def get_wards_areas(df):
    df["area"] = df.apply(get_lane_areas, axis=1)

    return df


def get_lane_areas(row):
    if 0.340 <= row.xcenter <= 0.419 and 0.095 <= row.ycenter <= 0.2:
        return "top1"
    if 0.253 <= row.xcenter <= 0.318 and 0.169 <= row.ycenter <= 0.239:
        return "top2"
    if 0.157 <= row.xcenter <= 0.245 and 0.200 <= row.ycenter <= 0.286:
        return "top3"
    if 0.113 <= row.xcenter <= 0.200 and 0.052 <= row.ycenter <= 0.1:
        return "top4"
    if 0.082 <= row.xcenter <= 0.122 and 0.101 <= row.ycenter <= 0.143:
        return "top5"
    if 0.048 <= row.xcenter <= 0.081 and 0.139 <= row.ycenter <= 0.195:
        return "top6"
    if 0.095 <= row.xcenter <= 0.175 and 0.310 <= row.ycenter <= 0.395:
        return "top7"
    if 0.179 <= row.xcenter <= 0.262 and 0.365 <= row.ycenter <= 0.421:
        return "top8"
    if 0.160 <= row.xcenter <= 0.279 and 0.422 <= row.ycenter <= 0.493:
        return "top9"

    if 0.427 <= row.xcenter <= 0.538 and 0.613 <= row.ycenter <= 0.704:
        return "mid1"
    if 0.539 <= row.xcenter <= 0.594 and 0.604 <= row.ycenter <= 0.696:
        return "mid2"
    if (0.528 <= row.xcenter <= 0.594 and 0.543 <= row.ycenter <= 0.603) or\
            (0.595 <= row.xcenter <= 0.677 and 0.543 <= row.ycenter <= 0.635):
        return "mid3"
    if 0.624 <= row.xcenter <= 0.704 and 0.447 <= row.ycenter <= 0.542:
        return "mid4"
    if (0.435 <= row.xcenter <= 0.505 and 0.485 <= row.ycenter <= 0.553) or \
            (0.506 <= row.xcenter <= 0.565 and 0.436 <= row.ycenter <= 0.505):
        return "mid5"
    if 0.462 <= row.xcenter <= 0.568 and 0.291 <= row.ycenter <= 0.379:
        return "mid6"
    if 0.406 <= row.xcenter <= 0.461 and 0.295 <= row.ycenter <= 0.392:
        return "mid7"
    if (0.406 <= row.xcenter <= 0.472 and 0.393 <= row.ycenter <= 0.457) or \
            (0.318 <= row.xcenter <= 0.405 and 0.352 <= row.ycenter <= 0.457):
        return "mid8"
    if 0.292 <= row.xcenter <= 0.376 and 0.460 <= row.ycenter <= 0.548:
        return "mid9"

    if 0.515 <= row.xcenter <= 0.642 and 0.795 <= row.ycenter <= 0.9:
        return "bot1"
    if 0.663 <= row.xcenter <= 0.734 and 0.760 <= row.ycenter <= 0.822:
        return "bot2"
    if 0.764 <= row.xcenter <= 0.839 and 0.704 <= row.ycenter <= 0.779:
        return "bot3"
    if 0.777 <= row.xcenter <= 0.861 and 0.830 <= row.ycenter <= 0.931:
        return "bot4"
    if 0.862 <= row.xcenter <= 0.913 and 0.847 <= row.ycenter <= 0.896:
        return "bot5"
    if 0.864 <= row.xcenter <= 0.939 and 0.773 <= row.ycenter <= 0.846:
        return "bot6"
    if 0.825 <= row.xcenter <= 0.887 and 0.617 <= row.ycenter <= 0.679:
        return "bot7"
    if 0.742 <= row.xcenter <= 0.824 and 0.578 <= row.ycenter <= 0.644:
        return "bot8"
    if 0.764 <= row.xcenter <= 0.878 and 0.500 <= row.ycenter <= 0.574:
        return "bot9"

    return "none"

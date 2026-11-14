# IAB content taxonomy mapping: Version 1.0 to 2.2

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/TaxonomyMapping
- Retrieved: 2026-11-14
- Category: Guides

---

# IAB content taxonomy mapping: Version 1.0 to 2.2

The Trade Desk has updated its content taxonomy categories to support both IAB 1.0 and IAB 2.2. If you are using the IAB 1.0 taxonomy for blocked categories (`bcat`), use the following tables to map these categories to IAB 2.2 and find the correct values for the `bcat` field.

To use these tables, look up the desired IAB 1.0 ID, then find the corresponding IAB 2.2 ID in the same row. Keep in mind that the IAB 2.2 taxonomy is more granular than the IAB 1.0 taxonomy. Some categories from the IAB 1.0 taxonomy map directly to a single category in IAB 2.2 (1:1 relationship), while others map to multiple categories (1:N relationships). For example, to block the "Arts & Entertainment" category, instead of using the IAB 1.0 ID of `IAB1`, use any or all of the IAB 2.2 IDs, such as `156` and `158` for musicals and nightclubs.

The categories in the following tables are organized first by IAB 1.0 ID in ascending order, and then alphabetically based on the IAB 2.2 category name. This reference excludes IAB24 and IAB25, which are uncategorized and unavailable for use, and includes IAB27, a custom category for medical health not in the original IAB definition.

> **TIP**: To quickly find your categories, enter keywords or the IDs in the search function of your web browser.

## IAB1

The following table lists categories with the top-level IAB1 ID.

| IAB 1.0 ID | IAB 1.0 Category Name | IAB 2.2 ID | IAB 2.2 Category Name |
| --- | --- | --- | --- |
| IAB1 | Arts & Entertainment | 150 | Events and Attractions |
| IAB1 | Arts & Entertainment | 93 | Entertainment Industry |
| IAB1 | Arts & Entertainment | 156 | Musicals |
| IAB1 | Arts & Entertainment | 158 | Nightclubs |
| IAB1 | Arts & Entertainment | 161 | Party Supplies and Decorations |
| IAB1-1 | Books & Literature | 43 | Art and Photography Books |
| IAB1-1 | Books & Literature | 44 | Biographies |
| IAB1-1 | Books & Literature | 42 | Books and Literature |
| IAB1-1 | Books & Literature | 45 | Children's Literature |
| IAB1-1 | Books & Literature | 46 | Comics and Graphic Novels |
| IAB1-1 | Books & Literature | 47 | Cookbooks |
| IAB1-1 | Books & Literature | 48 | Fiction |
| IAB1-1 | Books & Literature | 49 | Poetry |
| IAB1-1 | Books & Literature | 50 | Travel Books |
| IAB1-1 | Books & Literature | 51 | Young Adult Literature |
| IAB1-2 | Celebrity Fan/Gossip | 162 | Awards Shows |
| IAB1-2 | Celebrity Fan/Gossip | 433 | Celebrity Deaths |
| IAB1-2 | Celebrity Fan/Gossip | 434 | Celebrity Families |
| IAB1-2 | Celebrity Fan/Gossip | 435 | Celebrity Homes |
| IAB1-2 | Celebrity Fan/Gossip | 436 | Celebrity Pregnancy |
| IAB1-2 | Celebrity Fan/Gossip | 437 | Celebrity Relationships |
| IAB1-2 | Celebrity Fan/Gossip | 438 | Celebrity Scandal |
| IAB1-2 | Celebrity Fan/Gossip | 439 | Celebrity Style |
| IAB1-2 | Celebrity Fan/Gossip | 185 | Fan Conventions |
| IAB1-2 | Celebrity Fan/Gossip | 152 | Fashion Events |
| IAB1-2 | Celebrity Fan/Gossip | 432 | Pop Culture |
| IAB1-2 | Celebrity Fan/Gossip | 177 | Theater Venues and Events |
| IAB1-3 | Fine Art | 202 | Costume |
| IAB1-3 | Fine Art | 203 | Dance |
| IAB1-3 | Fine Art | 204 | Design |
| IAB1-3 | Fine Art | 201 | Fine Art |
| IAB1-3 | Fine Art | 206 | Fine Art Photography |
| IAB1-3 | Fine Art | 207 | Modern Art |
| IAB1-3 | Fine Art | 208 | Opera |
| IAB1-3 | Fine Art | 209 | Theater |
| IAB1-4 | Humor | 440 | Humor and Satire |
| IAB1-5 | Movies | 325 | Action and Adventure Movies |
| IAB1-5 | Movies | 329 | Animation Movies |
| IAB1-5 | Movies | 182 | Cinemas and Events |
| IAB1-5 | Movies | 330 | Comedy Movies |
| IAB1-5 | Movies | 331 | Crime and Mystery Movies |
| IAB1-5 | Movies | 332 | Documentary Movies |
| IAB1-5 | Movies | 333 | Drama Movies |
| IAB1-5 | Movies | 334 | Family and Children Movies |
| IAB1-5 | Movies | 335 | Fantasy Movies |
| IAB1-5 | Movies | 336 | Horror Movies |
| IAB1-5 | Movies | 324 | Movies |
| IAB1-5 | Movies | 326 | Romance Movies |
| IAB1-5 | Movies | 327 | Science Fiction Movies |
| IAB1-5 | Movies | 328 | Special Interest Movies |
| IAB1-5 | Movies | 177 | Theater Venues and Events |
| IAB1-5 | Movies | 337 | World Movies |
| IAB1-6 | Music | 342 | Adult Album Alternative |
| IAB1-6 | Music | 364 | Album-oriented Rock |
| IAB1-6 | Music | 343 | Alternative Music |
| IAB1-6 | Music | 365 | Alternative Rock |
| IAB1-6 | Music | 360 | Blues |
| IAB1-6 | Music | 345 | Classic Hits |
| IAB1-6 | Music | 346 | Classical Music |
| IAB1-6 | Music | 366 | Classic Rock |
| IAB1-6 | Music | 344 | Children's Music |
| IAB1-6 | Music | 347 | College Radio |
| IAB1-6 | Music | 348 | Comedy (Music and Audio) |
| IAB1-6 | Music | 184 | Concerts & Music Events |
| IAB1-6 | Music | 349 | Contemporary Hits/Pop/Top 40 |
| IAB1-6 | Music | 350 | Country Music |
| IAB1-6 | Music | 351 | Dance and Electronic Music |
| IAB1-6 | Music | 354 | Gospel Music |
| IAB1-6 | Music | 367 | Hard Rock |
| IAB1-6 | Music | 355 | Hip Hop Music |
| IAB1-6 | Music | 356 | Inspirational/New Age Music |
| IAB1-6 | Music | 357 | Jazz |
| IAB1-6 | Music | 338 | Music and Audio |
| IAB1-6 | Music | 358 | Oldies/Adult Standards |
| IAB1-6 | Music | 359 | Reggae |
| IAB1-6 | Music | 361 | Religious (Music and Audio) |
| IAB1-6 | Music | 362 | R&B/Soul/Funk |
| IAB1-6 | Music | 340 | Soft AC Music |
| IAB1-6 | Music | 368 | Soft Rock |
| IAB1-6 | Music | 369 | Soundtracks, TV and Showtunes |
| IAB1-6 | Music | 370 | Sports Radio |
| IAB1-6 | Music | 353 | Songwriters/Folk |
| IAB1-6 | Music | 177 | Theater Venues and Events |
| IAB1-6 | Music | 377 | Urban Contemporary Music |
| IAB1-6 | Music | 341 | Urban AC Music |
| IAB1-6 | Music | 378 | Variety (Music and Audio) |
| IAB1-6 | Music | 352 | World/International Music |
| IAB1-6 | Music | 372 | Business News Radio |
| IAB1-7 | Television | 641 | Animation TV |
| IAB1-7 | Television | 645 | Children's TV |
| IAB1-7 | Television | 646 | Comedy TV |
| IAB1-7 | Television | 647 | Drama TV |
| IAB1-7 | Television | 648 | Factual TV |
| IAB1-7 | Television | 649 | Holiday TV |
| IAB1-7 | Television | 650 | Music TV |
| IAB1-7 | Television | 651 | Reality TV |
| IAB1-7 | Television | 652 | Science Fiction TV |
| IAB1-7 | Television | 642 | Soap Opera TV |
| IAB1-7 | Television | 643 | Special Interest TV |
| IAB1-7 | Television | 644 | Sports TV |
| IAB1-7 | Television | 640 | Television |

## IAB2

The following table lists categories with the top-level IAB2 ID.

| IAB 1.0 ID | IAB 1.0 Category Name | IAB 2.2 ID | IAB 2.2 Category Name |
| --- | --- | --- | --- |
| IAB2 | Automotive | 38 | Auto Infotainment Technologies |
| IAB2 | Automotive | 31 | Auto Insurance |
| IAB2 | Automotive | 39 | Auto Navigation Systems |
| IAB2 | Automotive | 33 | Auto Recalls |
| IAB2 | Automotive | 41 | Auto Rentals |
| IAB2 | Automotive | 35 | Auto Safety |
| IAB2 | Automotive | 40 | Auto Safety Technologies |
| IAB2 | Automotive | 36 | Auto Shows |
| IAB2 | Automotive | 1 | Automotive |
| IAB2 | Automotive | 17 | Budget Cars |
| IAB2 | Automotive | 20 | Concept Cars |
| IAB2 | Automotive | 26 | Dash Cam Videos |
| IAB2 | Automotive | 21 | Driverless Cars |
| IAB2 | Automotive | 12 | Microcar |
| IAB2 | Automotive | 6 | SUV |
| IAB2 | Automotive | 7 | Van |
| IAB2-1 | Auto Parts | 32 | Auto Parts |
| IAB2-1 | Auto Parts | 26 | Dash Cam Videos |
| IAB2-2 | Auto Repair | 34 | Auto Repair |
| IAB2-3 | Buying/Selling Cars | 30 | Auto Buying and Selling |
| IAB2-4 | Car Culture | 25 | Car Culture |
| IAB2-5 | Certified Pre-Owned | 18 | Certified Pre-Owned Cars |
| IAB2-6 | Convertible | 8 | Convertible |
| IAB2-7 | Coupe | 9 | Coupe |
| IAB2-8 | Crossover | 10 | Crossover |
| IAB2-10 | Electric Vehicle | 22 | Green Vehicles |
| IAB2-11 | Hatchback | 11 | Hatchback |
| IAB2-12 | Hybrid | 22 | Green Vehicles |
| IAB2-13 | Luxury | 23 | Luxury Cars |
| IAB2-14 | MiniVan | 13 | Minivan |
| IAB2-15 | Motorcycles | 27 | Motorcycles |
| IAB2-15 | Motorcycles | 29 | Scooters |
| IAB2-16 | Off-Road Vehicles | 14 | Off-Road Vehicles |
| IAB2-17 | Performance Vehicles | 24 | Performance Cars |
| IAB2-18 | Pickup | 15 | Pickup Trucks |
| IAB2-19 | Road-Side Assistance | 28 | Road-Side Assistance |
| IAB2-20 | Sedan | 4 | Sedan |
| IAB2-21 | Trucks & Accessories | 3 | Commercial Trucks |
| IAB2-22 | Vintage Cars | 19 | Classic Cars |
| IAB2-23 | Wagon | 5 | Station Wagon |

## IAB3

The following table lists categories with the top-level IAB3 ID.

| IAB 1.0 ID | IAB 1.0 Category Name | IAB 2.2 ID | IAB 2.2 Category Name |
| --- | --- | --- | --- |
| IAB3 | Business | 64 | Angel Investment |
| IAB3 | Business | 113 | Apparel Industry |
| IAB3 | Business | 118 | Aviation Industry |
| IAB3 | Business | 65 | Bankruptcy |
| IAB3 | Business | 62 | Business Administration |
| IAB3 | Business | 54 | Business Accounting & Finance |
| IAB3 | Business | 72 | Business I.T. |
| IAB3 | Business | 66 | Business Loans |
| IAB3 | Business | 73 | Business Operations |
| IAB3 | Business | 79 | Business Utilities |
| IAB3 | Business | 120 | Civil Engineering Industry |
| IAB3 | Business | 81 | Commodities |
| IAB3 | Business | 67 | Debt Factoring & Invoice Discounting |
| IAB3 | Business | 122 | Defense Industry |
| IAB3 | Business | 76 | Executive Leadership & Management |
| IAB3 | Business | 95 | Financial Industry |
| IAB3 | Business | 98 | Hospitality Industry |
| IAB3 | Business | 99 | Information Services Industry |
| IAB3 | Business | 89 | Job Market |
| IAB3 | Business | 56 | Large Business |
| IAB3 | Business | 103 | Management Consulting Industry |
| IAB3 | Business | 104 | Manufacturing Industry |
| IAB3 | Business | 105 | Mechanical and Industrial Engineering Industry |
| IAB3 | Business | 106 | Media Industry |
| IAB3 | Business | 68 | Mergers and Acquisitions |
| IAB3 | Business | 108 | Non-Profit Organizations |
| IAB3 | Business | 110 | Power and Energy Industry |
| IAB3 | Business | 69 | Private Equity |
| IAB3 | Business | 111 | Publishing Industry |
| IAB3 | Business | 75 | Recalls |
| IAB3 | Business | 114 | Retail Industry |
| IAB3 | Business | 59 | Sales |
| IAB3 | Business | 70 | Sale & Lease Back |
| IAB3 | Business | 60 | Small and Medium-sized Business |
| IAB3 | Business | 61 | Startups |
| IAB3 | Business | 115 | Technology Industry |
| IAB3 | Business | 116 | Telecommunications Industry |
| IAB3 | Business | 71 | Venture Capital |
| IAB3-1 | Advertising | 91 | Advertising Industry |
| IAB3-1 | Advertising | 58 | Marketing and Advertising |
| IAB3-2 | Agriculture | 102 | Agriculture |
| IAB3-3 | Biotech/Biomedical | 119 | Biotech and Biomedical Industry |
| IAB3-5 | Construction | 121 | Construction Industry |
| IAB3-7 | Government | 77 | Government Business |
| IAB3-8 | Green Solutions | 94 | Environmental Services Industry |
| IAB3-8 | Green Solutions | 78 | Green Solutions |
| IAB3-9 | Human Resources | 55 | Human Resources |
| IAB3-10 | Logistics | 57 | Logistics |
| IAB3-10 | Logistics | 101 | Logistics and Transportation Industry |
| IAB3-11 | Marketing | 58 | Marketing and Advertising |
| IAB3-12 | Metals | 107 | Metals Industry |

## IAB4

The following table lists categories with the top-level IAB4 ID.

| IAB 1.0 ID | IAB 1.0 Category Name | IAB 2.2 ID | IAB 2.2 Category Name |
| --- | --- | --- | --- |
| IAB4 | Careers | 124 | Apprenticeships |
| IAB4 | Careers | 123 | Careers |
| IAB4 | Careers | 131 | Vocational Training |
| IAB4-1 | Career Planning | 126 | Career Planning |
| IAB4-3 | Financial Aid | 395 | Student Financial Aid |
| IAB4-4 | Job Fairs | 128 | Job Fairs |
| IAB4-6 | Resume Writing/Advice | 129 | Resume Writing and Advice |
| IAB4-8 | Scholarships | 395 | Student Financial Aid |
| IAB4-9 | Telecommuting | 130 | Remote Working |
| IAB4-11 | Career Advice | 125 | Career Advice |

## IAB5

The following table lists categories with the top-level IAB5 ID.

| IAB 1.0 ID | IAB 1.0 Category Name | IAB 2.2 ID | IAB 2.2 Category Name |
| --- | --- | --- | --- |
| IAB5 | Education | 142 | Early Childhood Education |
| IAB5 | Education | 132 | Education |
| IAB5 | Education | 92 | Education Industry |
| IAB5 | Education | 148 | Online Education |
| IAB5 | Education | 144 | Standardized Testing |
| IAB5-1 | 7-12 Education | 135 | Secondary Education |
| IAB5-2 | Adult Education | 133 | Adult Education |
| IAB5-5 | College Life | 138 | College Planning |
| IAB5-5 | College Life | 141 | Undergraduate Education |
| IAB5-8 | Language Learning | 147 | Language Learning |
| IAB5-9 | Graduate School | 140 | Professional School |
| IAB5-10 | Homeschooling | 145 | Homeschooling |
| IAB5-11 | Homework/Study Tips | 146 | Homework and Study |
| IAB5-12 | K-6 Educators | 149 | Primary Education |
| IAB5-13 | Private School | 134 | Private School |
| IAB5-14 | Special Education | 136 | Special Education |

## IAB6

The following table lists categories with the top-level IAB6 ID.

| IAB 1.0 ID | IAB 1.0 Category Name | IAB 2.2 ID | IAB 2.2 Category Name |
| --- | --- | --- | --- |
| IAB6 | Family & Parenting | 187 | Bereavement |
| IAB6 | Family & Parenting | 186 | Family and Relationships |
| IAB6 | Family & Parenting | 200 | Single Life |
| IAB6-1 | Adoption | 193 | Adoption and Fostering |
| IAB6-2 | Babies & Toddlers | 196 | Parenting Babies and Toddlers |
| IAB6-3 | Daycare/Pre School | 194 | Daycare and Pre-School |
| IAB6-4 | Family Internet | 195 | Internet Safety |
| IAB6-5 | Parenting - K-6 Kids | 197 | Parenting Children Aged 4-11 |
| IAB6-6 | Parenting teens | 198 | Parenting Teens |
| IAB6-8 | Special Needs Kids | 199 | Special Needs Kids |
| IAB6-9 | Eldercare | 190 | Eldercare |

## IAB7

The following table lists categories with the top-level IAB7 ID.

| IAB 1.0 ID | IAB 1.0 Category Name | IAB 2.2 ID | IAB 2.2 Category Name |
| --- | --- | --- | --- |
| IAB7 | Health & Fitness | 303 | Birth Control |
| IAB7 | Health & Fitness | 323 | Cosmetic Medical Services |
| IAB7 | Health & Fitness | 294 | Eye and Vision Conditions |
| IAB7 | Health & Fitness | 299 | First Aid |
| IAB7 | Health & Fitness | 96 | Food Industry |
| IAB7 | Health & Fitness | 295 | Foot Health |
| IAB7 | Health & Fitness | 97 | Healthcare Industry |
| IAB7 | Health & Fitness | 223 | Healthy Living |
| IAB7 | Health & Fitness | 291 | Hormonal Disorders |
| IAB7 | Health & Fitness | 304 | Infertility |
| IAB7 | Health & Fitness | 286 | Medical Health |
| IAB7 | Health & Fitness | 319 | Medical Tests |
| IAB7 | Health & Fitness | 292 | Menopause |
| IAB7 | Health & Fitness | 320 | Pharmaceutical Drugs |
| IAB7 | Health & Fitness | 109 | Pharmaceutical Industry |
| IAB7 | Health & Fitness | 305 | Pregnancy |
| IAB7 | Health & Fitness | 308 | Sexual Conditions |
| IAB7 | Health & Fitness | 321 | Surgery |
| IAB7 | Health & Fitness | 322 | Vaccines |
| IAB7-1 | Exercise | 226 | Participant Sports |
| IAB7-2 | A.D.D. | 301 | Mental Health |
| IAB7-3 | AIDS/HIV | 297 | Infectious Diseases |
| IAB7-4 | Allergies | 288 | Allergies |
| IAB7-6 | Arthritis | 312 | Bone and Joint Conditions |
| IAB7-7 | Asthma | 300 | Lung and Respiratory Health |
| IAB7-8 | Autism/PDD | 301 | Mental Health |
| IAB7-9 | Bipolar Disorder | 301 | Mental Health |
| IAB7-10 | Brain Tumor | 313 | Brain and Nervous System Disorders |
| IAB7-11 | Cancer | 314 | Cancer |
| IAB7-12 | Cholesterol | 306 | Blood Disorders |
| IAB7-13 | Chronic Fatigue Syndrome | 313 | Brain and Nervous System Disorders |
| IAB7-15 | Cold & Flu | 315 | Cold and Flu |
| IAB7-16 | Deafness | 289 | Ear, Nose and Throat Conditions |
| IAB7-17 | Dental Care | 316 | Dental Health |
| IAB7-17 | Dental Care | 593 | Oral care |
| IAB7-18 | Depression | 301 | Mental Health |
| IAB7-19 | Dermatology | 309 | Skin and Dermatology |
| IAB7-20 | Diabetes | 317 | Diabetes |
| IAB7-21 | Epilepsy | 313 | Brain and Nervous System Disorders |
| IAB7-22 | GERD/Acid Reflux | 318 | Digestive Disorders |
| IAB7-23 | Headaches/Migraines | 313 | Brain and Nervous System Disorders |
| IAB7-24 | Heart Disease | 296 | Heart and Cardiovascular Diseases |
| IAB7-25 | Herbs for Health | 234 | Herbs and Supplements |
| IAB7-26 | Holistic Healing | 235 | Holistic Health |
| IAB7-27 | IBS/Crohn's Disease | 318 | Digestive Disorders |
| IAB7-29 | Incontinence | 318 | Digestive Disorders |
| IAB7-31 | Men's Health | 228 | Men's Health |
| IAB7-32 | Nutrition | 229 | Nutrition |
| IAB7-33 | Orthopedics | 312 | Bone and Joint Conditions |
| IAB7-34 | Panic/Anxiety Disorders | 301 | Mental Health |
| IAB7-35 | Pediatrics | 224 | Children's Health |
| IAB7-35 | Pediatrics | 223 | Healthy Living |
| IAB7-36 | Physical Therapy | 236 | Physical Therapy |
| IAB7-37 | Psychology/Psychiatry | 301 | Mental Health |
| IAB7-38 | Senior Health | 223 | Healthy Living |
| IAB7-38 | Senior Health | 230 | Senior Health |
| IAB7-40 | Sleep Disorders | 310 | Sleep Disorders |
| IAB7-41 | Smoking Cessation | 237 | Smoking Cessation |
| IAB7-42 | Substance Abuse | 311 | Substance Abuse |
| IAB7-43 | Thyroid Disease | 293 | Thyroid Disorders |
| IAB7-44 | Weight Loss | 231 | Weight Loss |
| IAB7-45 | Women's Health | 238 | Women's Health |

## IAB8

The following table lists categories with the top-level IAB8 ID.

| IAB 1.0 ID | IAB 1.0 Category Name | IAB 2.2 ID | IAB 2.2 Category Name |
| --- | --- | --- | --- |
| IAB8 | Food & Drink | 216 | Cooking |
| IAB8 | Food & Drink | 210 | Food & Drink |
| IAB8 | Food & Drink | 220 | Food Movements |
| IAB8-1 | American Cuisine | 214 | World Cuisines |
| IAB8-2 | Barbecues & Grilling | 215 | Barbecues and Grilling |
| IAB8-3 | Cajun/Creole | 214 | World Cuisines |
| IAB8-4 | Chinese Cuisine | 214 | World Cuisines |
| IAB8-5 | Cocktails/Beer | 211 | Alcoholic Beverages |
| IAB8-6 | Coffee/Tea | 222 | Non-Alcoholic Beverages |
| IAB8-7 | Cuisine-Specific | 214 | World Cuisines |
| IAB8-8 | Desserts & Baking | 217 | Desserts and Baking |
| IAB8-9 | Dining Out | 218 | Dining Out |
| IAB8-10 | Food Allergies | 219 | Food Allergies |
| IAB8-11 | French Cuisine | 214 | World Cuisines |
| IAB8-12 | Health/Lowfat Cooking | 221 | Healthy Cooking and Eating |
| IAB8-13 | Italian Cuisine | 214 | World Cuisines |
| IAB8-14 | Japanese Cuisine | 214 | World Cuisines |
| IAB8-15 | Mexican Cuisine | 214 | World Cuisines |
| IAB8-16 | Vegan | 212 | Vegan Diets |
| IAB8-17 | Vegetarian | 213 | Vegetarian Diets |
| IAB8-18 | Wine | 211 | Alcoholic Beverages |

## IAB9

The following table lists categories with the top-level IAB9 ID.

| IAB 1.0 ID | IAB 1.0 Category Name | IAB 2.2 ID | IAB 2.2 Category Name |
| --- | --- | --- | --- |
| IAB9 | Hobbies & Interests | 258 | Beekeeping |
| IAB9 | Hobbies & Interests | 150 | Events and Attractions |
| IAB9 | Hobbies & Interests | 239 | Hobbies & Interests |
| IAB9 | Hobbies & Interests | 242 | Model Toys |
| IAB9 | Hobbies & Interests | 247 | Workshops and Classes |
| IAB9-1 | Art/Technology | 240 | Antiquing and Antiques |
| IAB9-1 | Art/Technology | 205 | Digital Arts |
| IAB9-1 | Art/Technology | 268 | Video Production |
| IAB9-3 | Beadwork | 249 | Beadwork |
| IAB9-4 | Birdwatching | 259 | Birdwatching |
| IAB9-5 | Board Games/Puzzles | 270 | Board Games and Puzzles |
| IAB9-6 | Candle & Soap Making | 250 | Candle and Soap Making |
| IAB9-7 | Card Games | 271 | Card Games |
| IAB9-7 | Card Games | 181 | Casinos & Gambling |
| IAB9-8 | Chess | 270 | Board Games and Puzzles |
| IAB9-9 | Cigars | 260 | Cigars |
| IAB9-11 | Comic Books | 262 | Comic Books |
| IAB9-12 | Drawing/Sketching | 251 | Drawing and Sketching |
| IAB9-13 | Freelance Writing | 266 | Freelance Writing |
| IAB9-14 | Genealogy | 273 | Genealogy and Ancestry |
| IAB9-16 | Guitar | 243 | Musical Instruments |
| IAB9-17 | Home Recording | 265 | Audio Production |
| IAB9-19 | Jewelry Making | 252 | Jewelry Making |
| IAB9-20 | Magic & Illusion | 241 | Magic and Illusion |
| IAB9-21 | Needlework | 253 | Needlework |
| IAB9-22 | Painting | 254 | Painting |
| IAB9-23 | Photography | 255 | Photography |
| IAB9-24 | Radio | 245 | Radio Control |
| IAB9-25 | Roleplaying Games | 272 | Roleplaying Games |
| IAB9-26 | Sci-Fi & Fantasy | 246 | Sci-fi and Fantasy |
| IAB9-27 | Scrapbooking | 256 | Scrapbooking |
| IAB9-28 | Screenwriting | 267 | Screenwriting |
| IAB9-29 | Stamps & Coins | 263 | Stamps and Coins |
| IAB9-30 | Video & Computer Games | 686 | Action Video Games |
| IAB9-30 | Video & Computer Games | 691 | Action-Adventure Video Games |
| IAB9-30 | Video & Computer Games | 692 | Adventure Video Games |
| IAB9-30 | Video & Computer Games | 693 | Casual Games |
| IAB9-30 | Video & Computer Games | 681 | Console Games |
| IAB9-30 | Video & Computer Games | 694 | Educational Video Games |
| IAB9-30 | Video & Computer Games | 695 | Exercise and Fitness Video Games |
| IAB9-30 | Video & Computer Games | 683 | Mobile Games |
| IAB9-30 | Video & Computer Games | 684 | PC Games |
| IAB9-30 | Video & Computer Games | 687 | Role-Playing Video Games |
| IAB9-30 | Video & Computer Games | 688 | Simulation Video Games |
| IAB9-30 | Video & Computer Games | 689 | Sports Video Games |
| IAB9-30 | Video & Computer Games | 690 | Strategy Video Games |
| IAB9-30 | Video & Computer Games | 680 | Video Gaming |
| IAB9-30 | Video & Computer Games | 682 | eSports |
| IAB9-31 | Woodworking | 257 | Woodworking |

## IAB10

The following table lists categories with the top-level IAB10 ID.

| IAB 1.0 ID | IAB 1.0 Category Name | IAB 2.2 ID | IAB 2.2 Category Name |
| --- | --- | --- | --- |
| IAB10 | Home & Garden | 274 | Home & Garden |
| IAB10 | Home & Garden | 281 | Home Security |
| IAB10 | Home & Garden | 285 | Outdoor Decorating |
| IAB10 | Home & Garden | 277 | Smart Home |
| IAB10-1 | Appliances | 278 | Home Appliances |
| IAB10-2 | Entertaining | 279 | Home Entertaining |
| IAB10-3 | Environmental Safety | 282 | Indoor Environmental Quality |
| IAB10-4 | Gardening | 275 | Gardening |
| IAB10-5 | Home Repair | 280 | Home Improvement |
| IAB10-6 | Home Theater | 634 | Home Entertainment Systems |
| IAB10-7 | Interior Decorating | 283 | Interior Decorating |
| IAB10-8 | Landscaping | 284 | Landscaping |
| IAB10-9 | Remodeling & Construction | 276 | Remodeling & Construction |

## IAB11

The following table lists categories with the top-level IAB11 ID.

| IAB 1.0 ID | IAB 1.0 Category Name | IAB 2.2 ID | IAB 2.2 Category Name |
| --- | --- | --- | --- |
| IAB11 | Law, Gov't & Politics | 394 | Government Support and Welfare |
| IAB11 | Law, Gov't & Politics | 100 | Legal Services Industry |
| IAB11 | Law, Gov't & Politics | 379 | News and Politics |
| IAB11-1 | Immigration | 388 | Political Issues |
| IAB11-2 | Legal Issues | 383 | Law |
| IAB11-3 | U.S. Government Resources | 388 | Political Issues |
| IAB11-6 | Elections (Candidates and Issues) | 387 | Elections |

## IAB12

The following table lists categories with the top-level IAB12 ID.

| IAB 1.0 ID | IAB 1.0 Category Name | IAB 2.2 ID | IAB 2.2 Category Name |
| --- | --- | --- | --- |
| IAB12 | News | 1011 | Academic/Research Content |
| IAB12 | News | 1218 | Aggregated/Curated |
| IAB12 | News | 1012 | Chat/IM/Comments |
| IAB12 | News | 1215 | Content Source |
| IAB12 | News | 1010 | Content Type |
| IAB12 | News | 380 | Crime |
| IAB12 | News | 381 | Disasters |
| IAB12 | News | 1013 | Educational Content |
| IAB12 | News | 373 | Educational Radio |
| IAB12 | News | 1014 | Entertainment Content |
| IAB12 | News | 1015 | Feature |
| IAB12 | News | 86 | Gasoline Prices |
| IAB12 | News | 1016 | General Social |
| IAB12 | News | 1017 | Instructional Content |
| IAB12 | News | 1018 | Interactive Content |
| IAB12 | News | 1019 | Listings/Classifieds/Product Listings/Search Results |
| IAB12 | News | 1020 | News |
| IAB12 | News | 374 | News Radio |
| IAB12 | News | 379 | News and Politics |
| IAB12 | News | 375 | News/Talk Radio |
| IAB12 | News | 1216 | Professionally Produced |
| IAB12 | News | 376 | Public Radio |
| IAB12 | News | 1021 | Review |
| IAB12 | News | 1217 | User Generated |
| IAB12-1 | International News | 382 | International News |
| IAB12-2 | National News | 385 | National News |
| IAB12-3 | Local News | 384 | Local News |

## IAB13

The following table lists categories with the top-level IAB13 ID.

| IAB 1.0 ID | IAB 1.0 Category Name | IAB 2.2 ID | IAB 2.2 Category Name |
| --- | --- | --- | --- |
| IAB13 | Personal Finance | 392 | Consumer Banking |
| IAB13 | Personal Finance | 83 | Financial Crisis |
| IAB13 | Personal Finance | 84 | Financial Reform |
| IAB13 | Personal Finance | 85 | Financial Regulation |
| IAB13 | Personal Finance | 397 | Frugal Living |
| IAB13 | Personal Finance | 418 | Gas and Electric |
| IAB13 | Personal Finance | 419 | Internet Service Providers |
| IAB13 | Personal Finance | 391 | Personal Finance |
| IAB13 | Personal Finance | 420 | Phone Services |
| IAB13 | Personal Finance | 421 | Water Services |
| IAB13-2 | Credit/Debt & Loans | 406 | Credit Cards |
| IAB13-2 | Credit/Debt & Loans | 407 | Home Financing |
| IAB13-2 | Credit/Debt & Loans | 408 | Personal Loans |
| IAB13-2 | Credit/Debt & Loans | 409 | Student Loans |
| IAB13-3 | Financial News | 52 | Business and Finance |
| IAB13-4 | Financial Planning | 396 | Financial Planning |
| IAB13-5 | Hedge Fund | 411 | Hedge Funds |
| IAB13-6 | Insurance | 399 | Health Insurance |
| IAB13-6 | Insurance | 400 | Home Insurance |
| IAB13-6 | Insurance | 401 | Life Insurance |
| IAB13-6 | Insurance | 402 | Motor Insurance |
| IAB13-6 | Insurance | 403 | Pet Insurance |
| IAB13-6 | Insurance | 404 | Travel Insurance |
| IAB13-8 | Mutual Funds | 412 | Mutual Funds |
| IAB13-9 | Options | 413 | Options |
| IAB13-10 | Retirement Planning | 416 | Retirement Planning |
| IAB13-11 | Stocks | 414 | Stocks and Bonds |
| IAB13-12 | Tax Planning | 415 | Personal Taxes |

## IAB14

The following table lists categories with the top-level IAB14 ID.

| IAB 1.0 ID | IAB 1.0 Category Name | IAB 2.2 ID | IAB 2.2 Category Name |
| --- | --- | --- | --- |
| IAB14 | Society | 1032 | Abkhaz |
| IAB14 | Society | 1031 | Afar |
| IAB14 | Society | 1034 | Afrikaans |
| IAB14 | Society | 1035 | Akan |
| IAB14 | Society | 1179 | Albanian |
| IAB14 | Society | 1036 | Amharic |
| IAB14 | Society | 164 | Anniversary |
| IAB14 | Society | 1038 | Arabic |
| IAB14 | Society | 1037 | Aragonese |
| IAB14 | Society | 1093 | Armenian |
| IAB14 | Society | 1039 | Assamese |
| IAB14 | Society | 1040 | Avaric |
| IAB14 | Society | 1033 | Avestan |
| IAB14 | Society | 1041 | Aymara |
| IAB14 | Society | 1042 | Azerbaijani |
| IAB14 | Society | 166 | Baby Shower |
| IAB14 | Society | 167 | Bachelor Party |
| IAB14 | Society | 168 | Bachelorette Party |
| IAB14 | Society | 1048 | Bambara |
| IAB14 | Society | 1043 | Bashkir |
| IAB14 | Society | 1072 | Basque |
| IAB14 | Society | 1044 | Belarusian |
| IAB14 | Society | 1049 | Bengali |
| IAB14 | Society | 1046 | Bihari |
| IAB14 | Society | 169 | Birth |
| IAB14 | Society | 170 | Birthday |
| IAB14 | Society | 1047 | Bislama |
| IAB14 | Society | 1052 | Bosnian |
| IAB14 | Society | 1051 | Breton |
| IAB14 | Society | 1045 | Bulgarian |
| IAB14 | Society | 1140 | Burmese |
| IAB14 | Society | 180 | Business Expos & Conferences |
| IAB14 | Society | 1053 | Catalan |
| IAB14 | Society | 1055 | Chamorro |
| IAB14 | Society | 1054 | Chechen |
| IAB14 | Society | 1151 | Chichewa |
| IAB14 | Society | 1213 | Chinese |
| IAB14 | Society | 1060 | Chuvash |
| IAB14 | Society | 182 | Cinemas and Events |
| IAB14 | Society | 183 | Comedy Events |
| IAB14 | Society | 184 | Concerts & Music Events |
| IAB14 | Society | 1030 | Content Language |
| IAB14 | Society | 1120 | Cornish |
| IAB14 | Society | 1056 | Corsican |
| IAB14 | Society | 1057 | Cree |
| IAB14 | Society | 1090 | Croatian |
| IAB14 | Society | 1058 | Czech |
| IAB14 | Society | 1062 | Danish |
| IAB14 | Society | 1064 | Divehi |
| IAB14 | Society | 1146 | Dutch |
| IAB14 | Society | 1065 | Dzongkha |
| IAB14 | Society | 1068 | English |
| IAB14 | Society | 1069 | Esperanto |
| IAB14 | Society | 1071 | Estonian |
| IAB14 | Society | 150 | Events and Attractions |
| IAB14 | Society | 1066 | Ewe |
| IAB14 | Society | 185 | Fan Conventions |
| IAB14 | Society | 1077 | Faroese |
| IAB14 | Society | 1073 | Farsi |
| IAB14 | Society | 152 | Fashion Events |
| IAB14 | Society | 1076 | Fijian |
| IAB14 | Society | 1075 | Finnish |
| IAB14 | Society | 1078 | French |
| IAB14 | Society | 1074 | Fula |
| IAB14 | Society | 171 | Funeral |
| IAB14 | Society | 1082 | Galician |
| IAB14 | Society | 1124 | Ganda |
| IAB14 | Society | 1107 | Georgian |
| IAB14 | Society | 1063 | German |
| IAB14 | Society | 172 | Graduation |
| IAB14 | Society | 1067 | Greek |
| IAB14 | Society | 1083 | Guarani |
| IAB14 | Society | 1084 | Gujarati |
| IAB14 | Society | 1091 | Haitian |
| IAB14 | Society | 1086 | Hausa |
| IAB14 | Society | 1087 | Hebrew |
| IAB14 | Society | 1094 | Herero |
| IAB14 | Society | 1088 | Hindi |
| IAB14 | Society | 1089 | Hiri Motu |
| IAB14 | Society | 153 | Historic Site and Landmark Tours |
| IAB14 | Society | 1092 | Hungarian |
| IAB14 | Society | 1102 | Icelandic |
| IAB14 | Society | 1101 | Ido |
| IAB14 | Society | 1098 | Igbo |
| IAB14 | Society | 1096 | Indonesian |
| IAB14 | Society | 1095 | Interlingua |
| IAB14 | Society | 1097 | Interlingue |
| IAB14 | Society | 1104 | Inuktitut |
| IAB14 | Society | 1100 | Inupiaq |
| IAB14 | Society | 1080 | Irish |
| IAB14 | Society | 1103 | Italian |
| IAB14 | Society | 1105 | Japanese |
| IAB14 | Society | 1106 | Javanese |
| IAB14 | Society | 1112 | Kalaallisut |
| IAB14 | Society | 1114 | Kannada |
| IAB14 | Society | 1116 | Kanuri |
| IAB14 | Society | 1117 | Kashmiri |
| IAB14 | Society | 1111 | Kazakh |
| IAB14 | Society | 1113 | Khmer |
| IAB14 | Society | 1109 | Kikuyu |
| IAB14 | Society | 1167 | Kinyarwanda |
| IAB14 | Society | 1164 | Kirundi |
| IAB14 | Society | 1119 | Komi |
| IAB14 | Society | 1108 | Kongo |
| IAB14 | Society | 1115 | Korean |
| IAB14 | Society | 1118 | Kurdish |
| IAB14 | Society | 1110 | Kwanyama |
| IAB14 | Society | 1121 | Kyrgyz |
| IAB14 | Society | 1127 | Lao |
| IAB14 | Society | 1122 | Latin |
| IAB14 | Society | 1130 | Latvian |
| IAB14 | Society | 1125 | Limburgish |
| IAB14 | Society | 1126 | Lingala |
| IAB14 | Society | 1128 | Lithuanian |
| IAB14 | Society | 1129 | Luba-Katanga |
| IAB14 | Society | 1123 | Luxembourgish |
| IAB14 | Society | 1134 | Macedonian |
| IAB14 | Society | 1131 | Malagasy |
| IAB14 | Society | 1138 | Malay |
| IAB14 | Society | 1135 | Malayalam |
| IAB14 | Society | 154 | Malls & Shopping Centers |
| IAB14 | Society | 1139 | Maltese |
| IAB14 | Society | 1085 | Manx |
| IAB14 | Society | 1133 | Māori |
| IAB14 | Society | 1137 | Marathi |
| IAB14 | Society | 1132 | Marshallese |
| IAB14 | Society | 1136 | Mongolian |
| IAB14 | Society | 155 | Museums & Galleries |
| IAB14 | Society | 156 | Musicals |
| IAB14 | Society | 157 | National & Civic Holidays |
| IAB14 | Society | 1141 | Nauruan |
| IAB14 | Society | 1150 | Navajo |
| IAB14 | Society | 1145 | Ndonga |
| IAB14 | Society | 1144 | Nepali |
| IAB14 | Society | 158 | Nightclubs |
| IAB14 | Society | 1143 | Northern Ndebele |
| IAB14 | Society | 1171 | Northern Sami |
| IAB14 | Society | 1148 | Norwegian |
| IAB14 | Society | 1142 | Norwegian Bokmal |
| IAB14 | Society | 1147 | Norwegian Nynorsk |
| IAB14 | Society | 1099 | Nuosu |
| IAB14 | Society | 1152 | Occitan |
| IAB14 | Society | 1153 | Ojibwe |
| IAB14 | Society | 1059 | Old Church Slavonic |
| IAB14 | Society | 1155 | Oriya |
| IAB14 | Society | 1154 | Oromo |
| IAB14 | Society | 1156 | Ossetian |
| IAB14 | Society | 159 | Outdoor Activities |
| IAB14 | Society | 1158 | Pali |
| IAB14 | Society | 1160 | Pashto |
| IAB14 | Society | 1159 | Polish |
| IAB14 | Society | 174 | Political Event |
| IAB14 | Society | 1161 | Portuguese |
| IAB14 | Society | 173 | Prom |
| IAB14 | Society | 1157 | Punjabi |
| IAB14 | Society | 1162 | Quechua |
| IAB14 | Society | 175 | Religious Events |
| IAB14 | Society | 1165 | Romanian |
| IAB14 | Society | 1163 | Romansh |
| IAB14 | Society | 1166 | Russian |
| IAB14 | Society | 1176 | Samoan |
| IAB14 | Society | 1172 | Sango |
| IAB14 | Society | 1168 | Sanskrit |
| IAB14 | Society | 1169 | Sardinian |
| IAB14 | Society | 1081 | Scottish Gaelic |
| IAB14 | Society | 1180 | Serbian |
| IAB14 | Society | 1177 | Shona |
| IAB14 | Society | 1170 | Sindhi |
| IAB14 | Society | 1173 | Sinhala |
| IAB14 | Society | 1174 | Slovak |
| IAB14 | Society | 1175 | Slovene |
| IAB14 | Society | 1178 | Somali |
| IAB14 | Society | 1149 | Southern Ndebele |
| IAB14 | Society | 1182 | Southern Sotho |
| IAB14 | Society | 1070 | Spanish |
| IAB14 | Society | 176 | Sporting Events |
| IAB14 | Society | 1183 | Sundanese |
| IAB14 | Society | 1185 | Swahili |
| IAB14 | Society | 1181 | Swati |
| IAB14 | Society | 1184 | Swedish |
| IAB14 | Society | 1192 | Tagalog |
| IAB14 | Society | 1199 | Tahitian |
| IAB14 | Society | 1188 | Tajik |
| IAB14 | Society | 1186 | Tamil |
| IAB14 | Society | 1197 | Tatar |
| IAB14 | Society | 1187 | Telugu |
| IAB14 | Society | 1189 | Thai |
| IAB14 | Society | 1050 | Tibetan |
| IAB14 | Society | 1190 | Tigrinya |
| IAB14 | Society | 1194 | Tonga |
| IAB14 | Society | 1196 | Tsonga |
| IAB14 | Society | 1193 | Tswana |
| IAB14 | Society | 1195 | Turkish |
| IAB14 | Society | 1191 | Turkmen |
| IAB14 | Society | 1198 | Twi |
| IAB14 | Society | 1201 | Ukrainian |
| IAB14 | Society | 1202 | Urdu |
| IAB14 | Society | 1200 | Uyghur |
| IAB14 | Society | 1203 | Uzbek |
| IAB14 | Society | 1204 | Venda |
| IAB14 | Society | 1205 | Vietnamese |
| IAB14 | Society | 1206 | Volapuk |
| IAB14 | Society | 1207 | Walloon |
| IAB14 | Society | 1061 | Welsh |
| IAB14 | Society | 1079 | Western Frisian |
| IAB14 | Society | 1208 | Wolof |
| IAB14 | Society | 1209 | Xhosa |
| IAB14 | Society | 1210 | Yiddish |
| IAB14 | Society | 1211 | Yoruba |
| IAB14 | Society | 1212 | Zhuang |
| IAB14 | Society | 1214 | Zulu |

## IAB15

The following table lists categories with the top-level IAB15 ID.

| IAB 1.0 ID | IAB 1.0 Category Name | IAB 2.2 ID | IAB 2.2 Category Name |
| --- | --- | --- | --- |
| IAB15 | Science | 467 | Environment |
| IAB15 | Science | 468 | Genetics |
| IAB15 | Science | 464 | Science |
| IAB15-1 | Astrology | 456 | Astrology |
| IAB15-2 | Biology | 465 | Biological Sciences |
| IAB15-3 | Chemistry | 466 | Chemistry |
| IAB15-4 | Geology | 470 | Geology |
| IAB15-5 | Paranormal Phenomena | 244 | Paranormal Phenomena |
| IAB15-6 | Physics | 471 | Physics |
| IAB15-7 | Space/Astronomy | 472 | Space and Astronomy |
| IAB15-8 | Geography | 469 | Geography |
| IAB15-9 | Botany | 465 | Biological Sciences |
| IAB15-10 | Weather | 390 | Weather |

## IAB16

The following table lists categories with the top-level IAB16 ID.

| IAB 1.0 ID | IAB 1.0 Category Name | IAB 2.2 ID | IAB 2.2 Category Name |
| --- | --- | --- | --- |
| IAB16 | Pets | 422 | Pets |
| IAB16 | Pets | 428 | Pet Adoptions |
| IAB16 | Pets | 431 | Pet Supplies |
| IAB16-1 | Aquariums | 426 | Fish and Aquariums |
| IAB16-2 | Birds | 423 | Birds |
| IAB16-3 | Cats | 424 | Cats |
| IAB16-4 | Dogs | 425 | Dogs |
| IAB16-5 | Large Animals | 427 | Large Animals |
| IAB16-6 | Reptiles | 429 | Reptiles |
| IAB16-7 | Veterinary Medicine | 430 | Veterinary Medicine |

## IAB17

The following table lists categories with the top-level IAB17 ID.

| IAB 1.0 ID | IAB 1.0 Category Name | IAB 2.2 ID | IAB 2.2 Category Name |
| --- | --- | --- | --- |
| IAB17 | Sports | 534 | Badminton |
| IAB17 | Sports | 548 | Beach Volleyball |
| IAB17 | Sports | 550 | Bowling |
| IAB17 | Sports | 493 | Darts |
| IAB17 | Sports | 494 | Disabled Sports |
| IAB17 | Sports | 508 | Fantasy Sports |
| IAB17 | Sports | 509 | Field Hockey |
| IAB17 | Sports | 513 | Gymnastics |
| IAB17 | Sports | 517 | Lacrosse |
| IAB17 | Sports | 526 | Rowing |
| IAB17 | Sports | 532 | Snooker/Pool/Billiards |
| IAB17 | Sports | 535 | Softball |
| IAB17 | Sports | 536 | Squash |
| IAB17 | Sports | 483 | Sports |
| IAB17 | Sports | 551 | Sports Equipment |
| IAB17 | Sports | 540 | Track and Field |
| IAB17 | Sports | 543 | Water Polo |
| IAB17 | Sports | 544 | Weightlifting |
| IAB17 | Sports | 546 | Wrestling |
| IAB17-2 | Baseball | 545 | Baseball |
| IAB17-2 | Baseball | 490 | College Baseball |
| IAB17-3 | Bicycling | 492 | Cycling |
| IAB17-4 | Bodybuilding | 549 | Bodybuilding |
| IAB17-5 | Boxing | 485 | Boxing |
| IAB17-6 | Canoeing/Kayaking | 499 | Canoeing and Kayaking |
| IAB17-7 | Cheerleading | 486 | Cheerleading |
| IAB17-8 | Climbing | 500 | Climbing |
| IAB17-9 | Cricket | 491 | Cricket |
| IAB17-10 | Figure Skating | 510 | Figure Skating |
| IAB17-11 | Fly Fishing | 511 | Fishing Sports |
| IAB17-12 | Football | 484 | American Football |
| IAB17-12 | Football | 507 | Australian Rules Football |
| IAB17-12 | Football | 488 | College Football |
| IAB17-13 | Freshwater Fishing | 511 | Fishing Sports |
| IAB17-15 | Golf | 512 | Golf |
| IAB17-16 | Horse Racing | 181 | Casinos & Gambling |
| IAB17-16 | Horse Racing | 497 | Horse Racing |
| IAB17-18 | Hunting/Shooting | 514 | Hunting and Shooting |
| IAB17-19 | Inline Skating | 516 | Inline Skating |
| IAB17-20 | Martial Arts | 520 | Martial Arts |
| IAB17-21 | Mountain Biking | 492 | Cycling |
| IAB17-23 | Olympics | 522 | Summer Olympic Sports |
| IAB17-23 | Olympics | 523 | Winter Olympic Sports |
| IAB17-24 | Paintball | 501 | Paintball |
| IAB17-25 | Power & Motorcycles | 519 | Motorcycle Sports |
| IAB17-26 | Pro Basketball | 489 | College Basketball |
| IAB17-26 | Pro Basketball | 547 | Basketball |
| IAB17-27 | Pro Ice Hockey | 515 | Ice Hockey |
| IAB17-28 | Rodeo | 525 | Rodeo |
| IAB17-29 | Rugby | 528 | Rugby League |
| IAB17-29 | Rugby | 529 | Rugby Union |
| IAB17-30 | Running/Jogging | 227 | Running and Jogging |
| IAB17-31 | Sailing | 530 | Sailing |
| IAB17-32 | Saltwater Fishing | 511 | Fishing Sports |
| IAB17-33 | Scuba Diving | 495 | Diving |
| IAB17-33 | Scuba Diving | 502 | Scuba Diving |
| IAB17-34 | Skateboarding | 503 | Skateboarding |
| IAB17-35 | Skiing | 531 | Skiing |
| IAB17-36 | Snowboarding | 504 | Snowboarding |
| IAB17-37 | Surfing/Bodyboarding | 505 | Surfing and Bodyboarding |
| IAB17-38 | Swimming | 537 | Swimming |
| IAB17-39 | Table Tennis/Ping-Pong | 538 | Table Tennis |
| IAB17-40 | Tennis | 539 | Tennis |
| IAB17-41 | Volleyball | 541 | Volleyball |
| IAB17-42 | Walking | 542 | Walking |
| IAB17-43 | Waterski/Wakeboard | 506 | Waterskiing and Wakeboarding |
| IAB17-44 | World Soccer | 533 | Soccer |

## IAB18

The following table lists categories with the top-level IAB18 ID.

| IAB 1.0 ID | IAB 1.0 Category Name | IAB 2.2 ID | IAB 2.2 Category Name |
| --- | --- | --- | --- |
| IAB18 | Style & Fashion | 150 | Events and Attractions |
| IAB18 | Style & Fashion | 152 | Fashion Events |
| IAB18 | Style & Fashion | 161 | Party Supplies and Decorations |
| IAB18 | Style & Fashion | 595 | Street Style |
| IAB18 | Style & Fashion | 552 | Style & Fashion |
| IAB18-1 | Beauty | 591 | Bath and Shower |
| IAB18-1 | Beauty | 592 | Deodorant and Antiperspirant |
| IAB18-1 | Beauty | 554 | Hair Care |
| IAB18-1 | Beauty | 556 | Nail Care |
| IAB18-1 | Beauty | 557 | Natural and Organic Beauty |
| IAB18-1 | Beauty | 558 | Perfume and Fragrance |
| IAB18-1 | Beauty | 594 | Shaving |
| IAB18-1 | Beauty | 559 | Skin Care |
| IAB18-2 | Body Art | 574 | Body Art |
| IAB18-2 | Body Art | 555 | Makeup and Accessories |
| IAB18-3 | Fashion | 577 | Fashion Trends |
| IAB18-3 | Fashion | 578 | High Fashion |
| IAB18-4 | Jewelry | 581 | Men's Jewelry and Watches |
| IAB18-4 | Jewelry | 565 | Women's Jewelry and Watches |
| IAB18-5 | Clothing | 575 | Children's Clothing |
| IAB18-5 | Clothing | 576 | Designer Clothing |
| IAB18-5 | Clothing | 583 | Men's Business Wear |
| IAB18-5 | Clothing | 584 | Men's Casual Wear |
| IAB18-5 | Clothing | 585 | Men's Formal Wear |
| IAB18-5 | Clothing | 586 | Men's Outerwear |
| IAB18-5 | Clothing | 589 | Men's Shoes and Footwear |
| IAB18-5 | Clothing | 587 | Men's Sportswear |
| IAB18-5 | Clothing | 588 | Men's Underwear and Sleepwear |
| IAB18-5 | Clothing | 567 | Women's Business Wear |
| IAB18-5 | Clothing | 568 | Women's Casual Wear |
| IAB18-5 | Clothing | 569 | Women's Formal Wear |
| IAB18-5 | Clothing | 562 | Women's Glasses |
| IAB18-5 | Clothing | 563 | Women's Handbags and Wallets |
| IAB18-5 | Clothing | 564 | Women's Hats and Scarves |
| IAB18-5 | Clothing | 570 | Women's Intimates and Sleepwear |
| IAB18-5 | Clothing | 571 | Women's Outerwear |
| IAB18-5 | Clothing | 573 | Women's Shoes and Footwear |
| IAB18-5 | Clothing | 572 | Women's Sportswear |
| IAB18-6 | Accessories | 591 | Bath and Shower |
| IAB18-6 | Accessories | 555 | Makeup and Accessories |

## IAB19

The following table lists categories with the top-level IAB19 ID.

| IAB 1.0 ID | IAB 1.0 Category Name | IAB 2.2 ID | IAB 2.2 Category Name |
| --- | --- | --- | --- |
| IAB19 | Technology & Computing | 597 | Artificial Intelligence |
| IAB19 | Technology & Computing | 1023 | Audio |
| IAB19 | Technology & Computing | 598 | Augmented Reality |
| IAB19 | Technology & Computing | 1000 | Content Channel |
| IAB19 | Technology & Computing | 1022 | Content Media Format |
| IAB19 | Technology & Computing | 617 | Desktops |
| IAB19 | Technology & Computing | 1001 | Editorial/Professional |
| IAB19 | Technology & Computing | 1002 | Email |
| IAB19 | Technology & Computing | 1003 | Forum/Community |
| IAB19 | Technology & Computing | 1004 | Game |
| IAB19 | Technology & Computing | 1024 | Images/Galleries |
| IAB19 | Technology & Computing | 1025 | Interactive |
| IAB19 | Technology & Computing | 630 | Laptops |
| IAB19 | Technology & Computing | 1005 | Marketplace/eCommerce |
| IAB19 | Technology & Computing | 1026 | Mixed |
| IAB19 | Technology & Computing | 638 | Robotics |
| IAB19 | Technology & Computing | 1006 | Search Engine/Listings |
| IAB19 | Technology & Computing | 1007 | Social |
| IAB19 | Technology & Computing | 596 | Technology & Computing |
| IAB19 | Technology & Computing | 1027 | Textual |
| IAB19 | Technology & Computing | 1008 | Utility/Online Tool |
| IAB19 | Technology & Computing | 1029 | VR/AR |
| IAB19 | Technology & Computing | 1028 | Video |
| IAB19 | Technology & Computing | 639 | Virtual Reality |
| IAB19 | Technology & Computing | 1009 | Voice Activated Channels |
| IAB19 | Technology & Computing | 637 | Wearable Technology |
| IAB19-1 | 3-D Graphics | 603 | 3-D Graphics |
| IAB19-2 | Animation | 610 | Computer Animation |
| IAB19-3 | Antivirus Software | 608 | Antivirus Software |
| IAB19-4 | C/C++ | 631 | Programming Languages |
| IAB19-4 | C/C++ | 621 | Web Development |
| IAB19-5 | Cameras & Camcorders | 633 | Cameras and Camcorders |
| IAB19-6 | Cell Phones | 635 | Smartphones |
| IAB19-8 | Computer Networking | 600 | Computer Networking |
| IAB19-9 | Computer Peripherals | 601 | Computer Peripherals |
| IAB19-11 | Data Centers | 620 | Cloud Computing |
| IAB19-11 | Data Centers | 616 | Data Storage and Warehousing |
| IAB19-11 | Data Centers | 622 | Web Hosting |
| IAB19-12 | Databases | 611 | Databases |
| IAB19-13 | Desktop Publishing | 612 | Desktop Publishing |
| IAB19-15 | Email | 623 | Email |
| IAB19-16 | Graphics Software | 614 | Graphics Software |
| IAB19-16 | Graphics Software | 604 | Photo Editing Software |
| IAB19-16 | Graphics Software | 606 | Video Software |
| IAB19-17 | Home Video/DVD | 634 | Home Entertainment Systems |
| IAB19-18 | Internet Technology | 609 | Browsers |
| IAB19-18 | Internet Technology | 620 | Cloud Computing |
| IAB19-18 | Internet Technology | 626 | IT and Internet Support |
| IAB19-18 | Internet Technology | 625 | Internet of Things |
| IAB19-18 | Internet Technology | 628 | Social Networking |
| IAB19-18 | Internet Technology | 621 | Web Development |
| IAB19-18 | Internet Technology | 622 | Web Hosting |
| IAB19-19 | Java | 631 | Programming Languages |
| IAB19-19 | Java | 621 | Web Development |
| IAB19-20 | JavaScript | 631 | Programming Languages |
| IAB19-20 | JavaScript | 621 | Web Development |
| IAB19-22 | MP3/MIDI | 613 | Digital Audio |
| IAB19-23 | Net Conferencing | 607 | Web Conferencing |
| IAB19-24 | Net for Beginners | 624 | Internet for Beginners |
| IAB19-25 | Network Security | 618 | Information and Network Security |
| IAB19-26 | Palmtops/PDAs | 636 | Tablets and E-readers |
| IAB19-29 | Entertainment | 686 | Action Video Games |
| IAB19-29 | Entertainment | 691 | Action-Adventure Video Games |
| IAB19-29 | Entertainment | 692 | Adventure Video Games |
| IAB19-29 | Entertainment | 693 | Casual Games |
| IAB19-29 | Entertainment | 681 | Console Games |
| IAB19-29 | Entertainment | 694 | Educational Video Games |
| IAB19-29 | Entertainment | 682 | eSports |
| IAB19-29 | Entertainment | 695 | Exercise and Fitness Video Games |
| IAB19-29 | Entertainment | 696 | MMOs |
| IAB19-29 | Entertainment | 683 | Mobile Games |
| IAB19-29 | Entertainment | 697 | Music and Party Video Games |
| IAB19-29 | Entertainment | 684 | PC Games |
| IAB19-29 | Entertainment | 698 | Puzzle Video Games |
| IAB19-29 | Entertainment | 687 | Role-Playing Video Games |
| IAB19-29 | Entertainment | 688 | Simulation Video Games |
| IAB19-29 | Entertainment | 689 | Sports Video Games |
| IAB19-29 | Entertainment | 690 | Strategy Video Games |
| IAB19-30 | Shareware/Freeware | 605 | Shareware and Freeware |
| IAB19-31 | Unix | 615 | Operating Systems |
| IAB19-32 | Visual Basic | 631 | Programming Languages |
| IAB19-32 | Visual Basic | 621 | Web Development |
| IAB19-34 | Web Design/HTML | 629 | Web Design and HTML |
| IAB19-34 | Web Design/HTML | 621 | Web Development |
| IAB19-35 | Web Search | 609 | Browsers |
| IAB19-35 | Web Search | 627 | Search |
| IAB19-36 | Windows | 615 | Operating Systems |

## IAB20

The following table lists categories with the top-level IAB20 ID.

| IAB 1.0 ID | IAB 1.0 Category Name | IAB 2.2 ID | IAB 2.2 Category Name |
| --- | --- | --- | --- |
| IAB20 | Travel | 1229 | Afghanistan |
| IAB20 | Travel | 1230 | Aland Islands |
| IAB20 | Travel | 1231 | Albania |
| IAB20 | Travel | 1232 | Algeria |
| IAB20 | Travel | 1233 | American Samoa |
| IAB20 | Travel | 1234 | Andorra |
| IAB20 | Travel | 1235 | Angola |
| IAB20 | Travel | 1236 | Anguilla |
| IAB20 | Travel | 1222 | Africa |
| IAB20 | Travel | 1225 | Antarctica |
| IAB20 | Travel | 1227 | Antarctica |
| IAB20 | Travel | 1237 | Antarctica |
| IAB20 | Travel | 1221 | Asia |
| IAB20 | Travel | 1242 | Australia |
| IAB20 | Travel | 1243 | Austria |
| IAB20 | Travel | 162 | Awards Shows |
| IAB20 | Travel | 1244 | Azerbaijan |
| IAB20 | Travel | 1245 | Bahrain |
| IAB20 | Travel | 1246 | Bangladesh |
| IAB20 | Travel | 1247 | Barbados |
| IAB20 | Travel | 179 | Bars & Restaurants |
| IAB20 | Travel | 673 | Beach Travel |
| IAB20 | Travel | 1251 | Benin |
| IAB20 | Travel | 1248 | Belarus |
| IAB20 | Travel | 1249 | Belgium |
| IAB20 | Travel | 1250 | Belize |
| IAB20 | Travel | 1252 | Bermuda |
| IAB20 | Travel | 1253 | Bhutan |
| IAB20 | Travel | 1255 | Bolivia |
| IAB20 | Travel | 1254 | Bolivarian Republic of Venezuela |
| IAB20 | Travel | 1256 | Bonaire, Sint Eustatius and Saba |
| IAB20 | Travel | 1257 | Bosnia and Herzegovina |
| IAB20 | Travel | 1258 | Botswana |
| IAB20 | Travel | 1259 | Bouvet Island |
| IAB20 | Travel | 1260 | Brazil |
| IAB20 | Travel | 1261 | British Virgin Islands |
| IAB20 | Travel | 1262 | Brunei Darussalam |
| IAB20 | Travel | 1263 | Bulgaria |
| IAB20 | Travel | 1264 | Burkina Faso |
| IAB20 | Travel | 1265 | Burundi |
| IAB20 | Travel | 1266 | Cabo Verde |
| IAB20 | Travel | 1267 | Cambodia |
| IAB20 | Travel | 1268 | Cameroon |
| IAB20 | Travel | 1269 | Canada |
| IAB20 | Travel | 1270 | Chad |
| IAB20 | Travel | 1271 | Chile |
| IAB20 | Travel | 1272 | China |
| IAB20 | Travel | 1273 | Christmas Island |
| IAB20 | Travel | 182 | Cinemas and Events |
| IAB20 | Travel | 1480 | City |
| IAB20 | Travel | 1274 | Colombia |
| IAB20 | Travel | 183 | Comedy Events |
| IAB20 | Travel | 184 | Concerts & Music Events |
| IAB20 | Travel | 1275 | Costa Rica |
| IAB20 | Travel | 1276 | Cote d'Ivoire |
| IAB20 | Travel | 1277 | Croatia |
| IAB20 | Travel | 1278 | Cuba |
| IAB20 | Travel | 1279 | Curaçao |
| IAB20 | Travel | 1280 | Cyprus |
| IAB20 | Travel | 1281 | Czechia |
| IAB20 | Travel | 679 | Day Trips |
| IAB20 | Travel | 1282 | Denmark |
| IAB20 | Travel | 1283 | Djibouti |
| IAB20 | Travel | 1284 | Dominica |
| IAB20 | Travel | 1285 | Ecuador |
| IAB20 | Travel | 1286 | Egypt |
| IAB20 | Travel | 1287 | El Salvador |
| IAB20 | Travel | 1288 | Equatorial Guinea |
| IAB20 | Travel | 1289 | Eritrea |
| IAB20 | Travel | 1290 | Estonia |
| IAB20 | Travel | 1291 | Ethiopia |
| IAB20 | Travel | 1226 | Europe |
| IAB20 | Travel | 150 | Events and Attractions |
| IAB20 | Travel | 185 | Fan Conventions |
| IAB20 | Travel | 1292 | Federated States of Micronesia |
| IAB20 | Travel | 1293 | Fiji |
| IAB20 | Travel | 1294 | Finland |
| IAB20 | Travel | 1295 | France |
| IAB20 | Travel | 1296 | French Guiana |
| IAB20 | Travel | 1297 | French Polynesia |
| IAB20 | Travel | 1298 | Gabon |
| IAB20 | Travel | 1299 | Georgia |
| IAB20 | Travel | 1300 | Germany |
| IAB20 | Travel | 1301 | Ghana |
| IAB20 | Travel | 1302 | Gibraltar |
| IAB20 | Travel | 1303 | Greece |
| IAB20 | Travel | 1304 | Greenland |
| IAB20 | Travel | 1305 | Grenada |
| IAB20 | Travel | 1306 | Guadeloupe |
| IAB20 | Travel | 1307 | Guam |
| IAB20 | Travel | 1308 | Guatemala |
| IAB20 | Travel | 1309 | Guernsey |
| IAB20 | Travel | 1310 | Guinea |
| IAB20 | Travel | 1311 | Guinea-Bissau |
| IAB20 | Travel | 1312 | Guyana |
| IAB20 | Travel | 1313 | Haiti |
| IAB20 | Travel | 1314 | Heard Island and McDonald Islands |
| IAB20 | Travel | 153 | Historic Site and Landmark Tours |
| IAB20 | Travel | 1315 | Honduras |
| IAB20 | Travel | 1316 | Hong Kong |
| IAB20 | Travel | 1317 | Hungary |
| IAB20 | Travel | 1318 | Iceland |
| IAB20 | Travel | 1319 | India |
| IAB20 | Travel | 1320 | Indonesia |
| IAB20 | Travel | 1321 | Iraq |
| IAB20 | Travel | 1322 | Ireland |
| IAB20 | Travel | 1323 | Islamic Republic of Iran |
| IAB20 | Travel | 1324 | Isle of Man |
| IAB20 | Travel | 1325 | Israel |
| IAB20 | Travel | 1326 | Italy |
| IAB20 | Travel | 1327 | Jamaica |
| IAB20 | Travel | 1328 | Japan |
| IAB20 | Travel | 1329 | Jersey |
| IAB20 | Travel | 1330 | Jordan |
| IAB20 | Travel | 1331 | Kazakhstan |
| IAB20 | Travel | 1332 | Kenya |
| IAB20 | Travel | 1333 | Kiribati |
| IAB20 | Travel | 1334 | Kuwait |
| IAB20 | Travel | 1335 | Kyrgyzstan |
| IAB20 | Travel | 1336 | Latvia |
| IAB20 | Travel | 1337 | Lebanon |
| IAB20 | Travel | 1338 | Lesotho |
| IAB20 | Travel | 1339 | Liberia |
| IAB20 | Travel | 1340 | Libya |
| IAB20 | Travel | 1341 | Liechtenstein |
| IAB20 | Travel | 1342 | Lithuania |
| IAB20 | Travel | 1343 | Luxembourg |
| IAB20 | Travel | 1344 | Macao |
| IAB20 | Travel | 1345 | Madagascar |
| IAB20 | Travel | 1346 | Malawi |
| IAB20 | Travel | 1347 | Malaysia |
| IAB20 | Travel | 1348 | Maldives |
| IAB20 | Travel | 1349 | Mali |
| IAB20 | Travel | 154 | Malls & Shopping Centers |
| IAB20 | Travel | 1350 | Malta |
| IAB20 | Travel | 1351 | Martinique |
| IAB20 | Travel | 1352 | Mauritania |
| IAB20 | Travel | 1353 | Mauritius |
| IAB20 | Travel | 1354 | Mayotte |
| IAB20 | Travel | 1479 | Metro |
| IAB20 | Travel | 1355 | Mexico |
| IAB20 | Travel | 1356 | Monaco |
| IAB20 | Travel | 1357 | Mongolia |
| IAB20 | Travel | 1358 | Montenegro |
| IAB20 | Travel | 1359 | Montserrat |
| IAB20 | Travel | 1360 | Morocco |
| IAB20 | Travel | 1361 | Mozambique |
| IAB20 | Travel | 155 | Museums & Galleries |
| IAB20 | Travel | 1362 | Myanmar |
| IAB20 | Travel | 1363 | Namibia |
| IAB20 | Travel | 157 | National & Civic Holidays |
| IAB20 | Travel | 1364 | Nauru |
| IAB20 | Travel | 1365 | Nepal |
| IAB20 | Travel | 1366 | New Caledonia |
| IAB20 | Travel | 1367 | New Zealand |
| IAB20 | Travel | 1368 | Nicaragua |
| IAB20 | Travel | 1369 | Nigeria |
| IAB20 | Travel | 158 | Nightclubs |
| IAB20 | Travel | 1370 | Niue |
| IAB20 | Travel | 1371 | Norfolk Island |
| IAB20 | Travel | 1223 | North America |
| IAB20 | Travel | 1372 | Norway |
| IAB20 | Travel | 1373 | Oman |
| IAB20 | Travel | 159 | Outdoor Activities |
| IAB20 | Travel | 1374 | Pakistan |
| IAB20 | Travel | 1375 | Palau |
| IAB20 | Travel | 1376 | Panama |
| IAB20 | Travel | 1377 | Papua New Guinea |
| IAB20 | Travel | 1378 | Paraguay |
| IAB20 | Travel | 160 | Parks & Nature |
| IAB20 | Travel | 161 | Party Supplies and Decorations |
| IAB20 | Travel | 1379 | Peru |
| IAB20 | Travel | 1380 | Pitcairn |
| IAB20 | Travel | 1381 | Poland |
| IAB20 | Travel | 661 | Polar Travel |
| IAB20 | Travel | 1382 | Portugal |
| IAB20 | Travel | 1383 | Puerto Rico |
| IAB20 | Travel | 1384 | Qatar |
| IAB20 | Travel | 669 | Rail Travel |
| IAB20 | Travel | 1478 | Region/State |
| IAB20 | Travel | 1385 | Reunion |
| IAB20 | Travel | 670 | Road Trips |
| IAB20 | Travel | 1386 | Romania |
| IAB20 | Travel | 1387 | Rwanda |
| IAB20 | Travel | 1388 | Saint Barthelemy |
| IAB20 | Travel | 1389 | Saint Helena, Ascension and Tristan da Cunha |
| IAB20 | Travel | 1390 | Saint Kitts and Nevis |
| IAB20 | Travel | 1391 | Saint Lucia |
| IAB20 | Travel | 1392 | Saint Martin |
| IAB20 | Travel | 1393 | Saint Pierre and Miquelon |
| IAB20 | Travel | 1394 | Saint Vincent and the Grenadines |
| IAB20 | Travel | 1395 | Samoa |
| IAB20 | Travel | 1396 | San Marino |
| IAB20 | Travel | 1397 | Sao Tome and Principe |
| IAB20 | Travel | 1398 | Saudi Arabia |
| IAB20 | Travel | 1399 | Senegal |
| IAB20 | Travel | 1400 | Serbia |
| IAB20 | Travel | 1401 | Seychelles |
| IAB20 | Travel | 1402 | Sierra Leone |
| IAB20 | Travel | 1403 | Singapore |
| IAB20 | Travel | 1404 | Sint Maarten |
| IAB20 | Travel | 1405 | Slovakia |
| IAB20 | Travel | 1406 | Slovenia |
| IAB20 | Travel | 1407 | Solomon Islands |
| IAB20 | Travel | 1408 | Somalia |
| IAB20 | Travel | 1409 | South Africa |
| IAB20 | Travel | 1224 | South America |
| IAB20 | Travel | 1410 | South Georgia and the South Sandwich Islands |
| IAB20 | Travel | 1411 | South Sudan |
| IAB20 | Travel | 1412 | Spain |
| IAB20 | Travel | 1413 | Sri Lanka |
| IAB20 | Travel | 1414 | State of Palestine |
| IAB20 | Travel | 1415 | Suriname |
| IAB20 | Travel | 1416 | Svalbard and Jan Mayen |
| IAB20 | Travel | 1417 | Swaziland |
| IAB20 | Travel | 1418 | Sweden |
| IAB20 | Travel | 1419 | Switzerland |
| IAB20 | Travel | 1420 | Syrian Arab Republic |
| IAB20 | Travel | 1421 | Taiwan (Province of China) |
| IAB20 | Travel | 1422 | Tajikistan |
| IAB20 | Travel | 1423 | Thailand |
| IAB20 | Travel | 1424 | The Bahamas |
| IAB20 | Travel | 1425 | The British Indian Ocean Territory |
| IAB20 | Travel | 1426 | The Cayman Islands |
| IAB20 | Travel | 1427 | The Central African Republic |
| IAB20 | Travel | 1428 | The Cocos Islands |
| IAB20 | Travel | 1429 | The Comoros |
| IAB20 | Travel | 1430 | The Congo |
| IAB20 | Travel | 1431 | The Cook Islands |
| IAB20 | Travel | 1432 | The Democratic People's Republic of Korea |
| IAB20 | Travel | 1433 | the Democratic Republic of the Congo |
| IAB20 | Travel | 1434 | The Dominican Republic |
| IAB20 | Travel | 1435 | The Falkland Islands |
| IAB20 | Travel | 1436 | The Faroe Islands |
| IAB20 | Travel | 1437 | The former Yugoslav Republic of Macedonia |
| IAB20 | Travel | 1438 | The French Southern Territories |
| IAB20 | Travel | 1439 | The Gambia |
| IAB20 | Travel | 1440 | The Holy See |
| IAB20 | Travel | 1441 | The Lao People's Democratic Republic |
| IAB20 | Travel | 1442 | The Marshall Islands |
| IAB20 | Travel | 1443 | The Netherlands |
| IAB20 | Travel | 1444 | The Niger |
| IAB20 | Travel | 1445 | The Northern Mariana Islands |
| IAB20 | Travel | 1446 | The Philippines |
| IAB20 | Travel | 1447 | The Republic of Korea |
| IAB20 | Travel | 1448 | The Republic of Moldova |
| IAB20 | Travel | 1449 | The Russian Federation |
| IAB20 | Travel | 1450 | The Sudan |
| IAB20 | Travel | 1451 | The Turks and Caicos Islands |
| IAB20 | Travel | 1452 | The United Arab Emirates |
| IAB20 | Travel | 1453 | The United Kingdom of Great Britain and Northern Ireland |
| IAB20 | Travel | 1454 | The United States Minor Outlying Islands |
| IAB20 | Travel | 1455 | The United States of America |
| IAB20 | Travel | 177 | Theater Venues and Events |
| IAB20 | Travel | 1456 | Timor-Leste |
| IAB20 | Travel | 1457 | Togo |
| IAB20 | Travel | 1458 | Tokelau |
| IAB20 | Travel | 1459 | Tonga |
| IAB20 | Travel | 653 | Travel |
| IAB20 | Travel | 654 | Travel Accessories |
| IAB20 | Travel | 663 | Travel Preparation and Advice |
| IAB20 | Travel | 1460 | Trinidad and Tobago |
| IAB20 | Travel | 1461 | Tunisia |
| IAB20 | Travel | 1462 | Turkey |
| IAB20 | Travel | 1463 | Turkmenistan |
| IAB20 | Travel | 1464 | Tuvalu |
| IAB20 | Travel | 1465 | U.S. Virgin Islands |
| IAB20 | Travel | 1466 | Uganda |
| IAB20 | Travel | 1467 | Ukraine |
| IAB20 | Travel | 1468 | United Republic of Tanzania |
| IAB20 | Travel | 1469 | Uruguay |
| IAB20 | Travel | 1470 | Uzbekistan |
| IAB20 | Travel | 1471 | Vanuatu |
| IAB20 | Travel | 1472 | Vietnam |
| IAB20 | Travel | 1473 | Wallis and Futuna |
| IAB20 | Travel | 1474 | Western Sahara |
| IAB20 | Travel | 1475 | Yemen |
| IAB20 | Travel | 1476 | Zambia |
| IAB20 | Travel | 1477 | Zimbabwe |
| IAB20-1 | Adventure Travel | 665 | Adventure Travel |
| IAB20-1 | Adventure Travel | 178 | Zoos & Aquariums |
| IAB20-2 | Africa | 656 | Africa Travel |
| IAB20-3 | Air Travel | 672 | Air Travel |
| IAB20-4 | Australia & New Zealand | 658 | Australia and Oceania Travel |
| IAB20-5 | Bed & Breakfasts | 674 | Bed & Breakfasts |
| IAB20-6 | Budget Travel | 675 | Budget Travel |
| IAB20-7 | Business Travel | 676 | Business Travel |
| IAB20-8 | By US Locale | 660 | North America Travel |
| IAB20-9 | Camping | 677 | Camping |
| IAB20-10 | Canada | 660 | North America Travel |
| IAB20-11 | Caribbean | 660 | North America Travel |
| IAB20-12 | Cruises | 678 | Cruises |
| IAB20-13 | Eastern Europe | 659 | Europe Travel |
| IAB20-14 | Europe | 659 | Europe Travel |
| IAB20-15 | France | 659 | Europe Travel |
| IAB20-16 | Greece | 659 | Europe Travel |
| IAB20-17 | Honeymoons/Getaways | 667 | Honeymoons and Getaways |
| IAB20-18 | Hotels | 668 | Hotels and Motels |
| IAB20-19 | Italy | 659 | Europe Travel |
| IAB20-20 | Japan | 657 | Asia Travel |
| IAB20-21 | Mexico & Central America | 662 | South America Travel |
| IAB20-22 | National Parks | 178 | Zoos & Aquariums |
| IAB20-23 | South America | 662 | South America Travel |
| IAB20-24 | Spas | 671 | Spas |
| IAB20-25 | Theme Parks | 151 | Amusement and Theme Parks |
| IAB20-25 | Theme Parks | 178 | Zoos & Aquariums |
| IAB20-26 | Traveling with Kids | 666 | Family Travel |
| IAB20-26 | Traveling with Kids | 178 | Zoos & Aquariums |
| IAB20-27 | United Kingdom | 659 | Europe Travel |

## IAB21

The following table lists categories with the top-level IAB21 ID.

| IAB 1.0 ID | IAB 1.0 Category Name | IAB 2.2 ID | IAB 2.2 Category Name |
| --- | --- | --- | --- |
| IAB21 | Real Estate | 445 | Developmental Sites |
| IAB21 | Real Estate | 446 | Hotel Properties |
| IAB21 | Real Estate | 447 | Houses |
| IAB21 | Real Estate | 87 | Housing Market |
| IAB21 | Real Estate | 448 | Industrial Property |
| IAB21 | Real Estate | 88 | Interest Rates |
| IAB21 | Real Estate | 449 | Land and Farms |
| IAB21 | Real Estate | 450 | Office Property |
| IAB21 | Real Estate | 441 | Real Estate |
| IAB21 | Real Estate | 112 | Real Estate Industry |
| IAB21 | Real Estate | 452 | Real Estate Renting and Leasing |
| IAB21 | Real Estate | 443 | Retail Property |
| IAB21 | Real Estate | 444 | Vacation Properties |
| IAB21-1 | Apartments | 442 | Apartments |
| IAB21-3 | Buying/Selling Homes | 451 | Real Estate Buying and Selling |

## IAB22

The following table lists categories with the top-level IAB22 ID.

| IAB 1.0 ID | IAB 1.0 Category Name | IAB 2.2 ID | IAB 2.2 Category Name |
| --- | --- | --- | --- |
| IAB22 | Shopping | 482 | Children's Games and Toys |
| IAB22 | Shopping | 475 | Flower Shopping |
| IAB22 | Shopping | 476 | Gifts and Greetings Cards |
| IAB22 | Shopping | 477 | Grocery Shopping |
| IAB22 | Shopping | 478 | Holiday Shopping |
| IAB22 | Shopping | 479 | Household Supplies |
| IAB22 | Shopping | 480 | Lotteries and Scratchcards |
| IAB22 | Shopping | 154 | Malls & Shopping Centers |
| IAB22 | Shopping | 473 | Shopping |
| IAB22-1 | Contests & Freebies | 481 | Sales and Promotions |
| IAB22-2 | Couponing | 474 | Coupons and Discounts |

## IAB23

The following table lists categories with the top-level IAB23 ID.

| IAB 1.0 ID | IAB 1.0 Category Name | IAB 2.2 ID | IAB 2.2 Category Name |
| --- | --- | --- | --- |
| IAB23 | Religion & Spirituality | 453 | Religion & Spirituality |
| IAB23 | Religion & Spirituality | 463 | Sikhism |
| IAB23-1 | Alternative Religions | 455 | Spirituality |
| IAB23-2 | Atheism/Agnosticism | 454 | Agnosticism |
| IAB23-2 | Atheism/Agnosticism | 457 | Atheism |
| IAB23-3 | Buddhism | 458 | Buddhism |
| IAB23-4 | Catholicism | 459 | Christianity |
| IAB23-5 | Christianity | 459 | Christianity |
| IAB23-6 | Hinduism | 460 | Hinduism |
| IAB23-7 | Islam | 461 | Islam |
| IAB23-8 | Judaism | 462 | Judaism |
| IAB23-9 | Latter-Day Saints | 459 | Christianity |
| IAB23-10 | Pagan/Wiccan | 453 | Religion & Spirituality |

## IAB26

The following table lists categories with the top-level IAB26 ID.

| IAB 1.0 ID | IAB 1.0 Category Name | IAB 2.2 ID | IAB 2.2 Category Name |
| --- | --- | --- | --- |
| IAB26-3 | Spyware/Malware | 608 | Antivirus Software |

## IAB27

The following table lists categories with the top-level IAB27 ID. This is a custom category for medical health not in the original IAB definition.

| IAB 1.0 ID | IAB 1.0 Category Name | IAB 2.2 ID | IAB 2.2 Category Name |
| --- | --- | --- | --- |
| IAB27 | Medical Health | 286 | Medical Health |
| IAB27-1 | Allergies | 288 | Allergies |
| IAB27-3 | Blood Disorders | 306 | Blood Disorders |
| IAB27-4 | Bone and Joint Conditions | 312 | Bone and Joint Conditions |
| IAB27-5 | Brain and Nervous System Disorders | 313 | Brain and Nervous System Disorders |
| IAB27-6 | Cancer | 314 | Cancer |
| IAB27-7 | Cold and Flu | 315 | Cold and Flu |
| IAB27-9 | Dental Health | 316 | Dental Health |
| IAB27-11 | Digestive Disorders | 318 | Digestive Disorders |
| IAB27-12 | Ear, Nose and Throat Conditions | 289 | Ear, Nose and Throat Conditions |
| IAB27-17 | Heart and Cardiovascular Diseases | 296 | Heart and Cardiovascular Diseases |
| IAB27-19 | Infectious Diseases | 297 | Infectious Diseases |
| IAB27-22 | Lung and Respiratory Health | 300 | Lung and Respiratory Health |
| IAB27-25 | Mental Health | 301 | Mental Health |
| IAB27-31 | Skin and Dermatology | 309 | Skin and Dermatology |
| IAB27-32 | Sleep Disorders | 310 | Sleep Disorders |
| IAB27-33 | Substance Abuse | 311 | Substance Abuse |
| IAB27-35 | Thyroid Disorders | 293 | Thyroid Disorders |

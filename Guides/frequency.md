# Frequency

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/Frequency
- Category: Guides

---

# Frequency

Frequency is the number of times a user sees an ad within a given time period.

> **NOTE**: Depending on the audience settings, the term "user" can refer to an ID, person, or household.

In the UI, the user is dependent on the cross-device setting selected in the Audience (**Au**) tile. In the API, the ID for the [cross-device graph](/v3/portal/api/doc/CrossDeviceTargeting) type can be specified in the following properties at the ad group level: `RTBAttributes.AudienceTargeting.CrossDeviceVendorListForAudience`.

There are several common ways of using frequency to optimize your bidding strategy for KPIs like reach, budget, or share of voice:

*   [Frequency caps](#frequency-caps)
*   [Frequency goals](#frequency-goals)
*   [Frequency bid adjustments](#frequency-bid-adjustment)

## 

Frequency Caps[](#frequency-caps)

A frequency cap, or an f-cap, limits the number of impressions a user can see within a given time period in a frequency cycle. Frequency caps are represented using fraction notation, where the numerator represents the number of impressions, and the denominator represents the frequency cycle interval, typically expressed in hours or minutes. For example, a 1/3-hour frequency cap indicates that a user can be served a maximum of 1 impression within each 3-hour time period.

> **IMPORTANT**: Even though fractions such as 1/1 and 4/4 are equivalent mathematically, they are not equivalent frequency caps. For details and examples, see [Understanding Fraction Notation and Pacing](#frequency-fractions).

Low frequency caps target a user with a small number of ads during campaign flights. In campaigns with excessively low frequency caps, users may not see enough content to impact the user's behavior or brand perception. Utilizing a frequency goal helps prevent this scenario.

## 

Frequency Goals[](#frequency-goals)

A frequency goal specifies the preferred number of impressions to be targeted for a user. The platform optimizes toward the number of impressions set as the frequency goal. For example, users who have already seen an ad are favored to see another impression over unknown users until the specified frequency goal is reached.

> **IMPORTANT**: Frequency goals must have the minimum range of 1 per 24 hours.

## 

Frequency Bid Adjustments[](#frequency-bid-adjustment)

Frequency bid adjustments update bid amounts for a user based on the number of impressions seen within the frequency cycle. A frequency range in a bid line specifies the minimum and maximum number of impressions to be shown to a user. Multiple bid adjustments for individual frequency ranges may be grouped to increase or decrease bidding for users who have seen an ad a certain number of times over a specified time period. For details, see [Frequency Bid Adjustments](/v3/portal/api/doc/FrequencyConfigurationBasicBidAdjustments).

## 

Frequency Framework[](#frequency-framework)

The platform frequency framework provides the flexibility for doing the following:

*   Decide how many user impressions to target.
*   Target user impressions at both campaign and ad group levels at the same time.
*   Customize which campaigns and/or ad groups increment a user's frequency count.
*   Create multiple frequency caps with different frequency intervals for a campaign and/or an ad group.
*   Decide to which campaigns or ad groups to assign frequency caps, frequency goals, bid adjustments, and reporting independently of the entities used to increment a user's frequency count.

### 

Frequency Framework Elements[](#frequency-elements)

There are three individually configurable elements that make up the frequency framework and allow better leveraging of the frequency cycle.

| Element | Definition |
| Counter | A container that holds the user’s frequency count information (the number of times the user has seen the ad) and defines the time interval (in minutes) after which the counter is reset. |
| Increment | An entity (partner, advertiser, campaign, and ad group) that serves impressions to users and increases the user's frequency count for the associated counter. |
| Bid List | Bid lists apply frequency settings to ad groups, campaigns, and other entities by associating the bid list with the entity and enabling the relationship for the entity.  
Use bid lists to define frequency caps, set frequency goals, and adjust bids based on the associated counter. |

> **TIP**: While these elements are individually configurable, for basic configurations, it is most efficient to use the [frequency configuration endpoints](/v3/portal/api/area/Frequency%20Config), which allow you to set up counters, increments, and bid lists in one step.

For details on how to create and manage each element, see [Frequency Management Tasks and APIs](/v3/portal/api/doc/FrequencyTasks).

## 

Understanding Fraction Notation and Pacing[](#frequency-fractions)

Frequency caps are often represented using fraction notation, where the numerator represents the number of impressions, and the denominator represents the frequency cycle interval, typically expressed in hours or minutes. This notation, however, may cause confusion regarding ad delivery. For example, fractions such as 4/4 and 1/1 are equivalent mathematically, but they are not equivalent frequency caps.

Setting a frequency cap as 4 ads within 4 hours (4/4) does not guarantee that the user will see ads evenly distributed throughout 4 hours. It is possible that an active user may hit their f-cap within the first minute and not be served ads for the remaining 3 hours and 59 minutes left on the counter. To ensure a more even delivery, it is better to set a frequency cap as 1 ad within 1 hour (1/1).

> **IMPORTANT**: Frequency cap numerators with the value of `1` allow the platform to space delivery more evenly and improve performance.

The following diagrams illustrate the distribution of impressions for the 4/4 and 1/1 frequency caps. Assuming a user is active every hour during these hours, the platform would deliver up to 8 ads within 8 hours in each use case.

The following diagrams illustrate the distribution of impressions for the same frequency caps but with the assumption that the user is online for a total of 4 hours within the 8-hour time period and is offline between hours 2 and 6.

## 

FAQs[](#frequency-faqs)

The following are some of the commonly asked questions about frequency.

### 

What’s the difference between a frequency cap and frequency goal?

A frequency cap limits the number of impressions a user can see within a certain time period. See also [Frequency Caps](/v3/portal/api/doc/FrequencyConfigurationBasicCaps).

A frequency goal aims to reach the user within the ad group the desired number of times. It is not guaranteed that this goal will be reached, as user behavior cannot be controlled. See also [Frequency Goals](/v3/portal/api/doc/FrequencyConfigurationBasicGoals).

### 

Does setting a frequency goal per interval mean the same users are retargeted for that interval?

No. After the first exposure, frequency goals work to prioritize bidding on the users seen before over new users to the ad group within the time interval selected. After the interval expires, the counter is reset and users become unknown again.

### 

What happens if a frequency cap is changed mid-cycle?

If a frequency cap is changed in the middle of a frequency cycle, the system keeps track of previous counts and applies them to the new frequency cap.

### 

How long does the lifetime frequency interval last?

For the duration of the flight of the ad group and two weeks of inactivity after it ends.
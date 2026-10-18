#!/usr/bin/env python3
"""
Adds PvP Arena Rationale & Matchup Counters to celestine, seraph, dullahan, orc, and elf.
"""

import os

PVP_EXTRA = {
    "celestine": """
      <!-- PvP Arena Combat Analysis -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #38bdf8; margin: 0 0 14px;">PvP Arena Matchups & Anti-Meta Strategies</h2>
        <p style="color: var(--muted); font-size: 0.95rem; line-height: 1.6; margin: 0 0 16px;">
          In competitive 3v3 Castle Arena duels, status afflictions like Stun, Silence, and Bleed determine match outcomes within the opening two turns. Celestine completely disrupts standard arena offensive openers:
        </p>
        <ul style="color: var(--muted); font-size: 0.9rem; line-height: 1.6; padding-left: 20px; margin: 0;">
          <li style="margin-bottom: 8px;">
            <strong style="color: #fff;">Countering Assassin Openers:</strong> Stealth Assassins rely on Turn 1 burst stuns. Celestine's 25% passive cleanse immediately purges stun locks, allowing your frontline tank to retaliate and protect fragile allies.
          </li>
          <li style="margin-bottom: 8px;">
            <strong style="color: #fff;">Negating Hexer Decay Stacks:</strong> Opposing Mage and Hexer teams inflict multi-turn decay curses. Divine Ward reduces incoming magical burst by 8%, while Aura of Grace ensures counter-healing restores allies faster than enemy DoTs can tick.
          </li>
          <li>
            <strong style="color: #fff;">Recommended Arena Role:</strong> Position in the secondary backline. Focus Turn 1 on applying Holy Ward to your primary damage dealer, ensuring their offensive burst cannot be interrupted by opposing crowd control.
          </li>
        </ul>
      </section>
""",
    "seraph": """
      <!-- PvP Arena Combat Analysis -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #c9a227; margin: 0 0 14px;">PvP Arena Matchups & Anti-Meta Strategies</h2>
        <p style="color: var(--muted); font-size: 0.95rem; line-height: 1.6; margin: 0 0 16px;">
          Speed dictates arena tempo. Because Seraph characters naturally possess the highest initiative values in Pixel Lineage, they dictate the opening engagement phase in Castle Arena duels:
        </p>
        <ul style="color: var(--muted); font-size: 0.9rem; line-height: 1.6; padding-left: 20px; margin: 0;">
          <li style="margin-bottom: 8px;">
            <strong style="color: #fff;">Guaranteed First-Strike Advantage:</strong> In 1v1 and 3v3 brackets, having +10% Speed ensures you take action before enemy tanks can activate defensive postures or cast damage barriers.
          </li>
          <li style="margin-bottom: 8px;">
            <strong style="color: #fff;">Armor-Piercing Tank Shred:</strong> Opposing Sentinel Warriors stacking heavy plate often boast 70%+ physical mitigation. Seraph's 8% True Damage on hit ignores all armor values, consistently chipping down turtle compositions that other physical classes cannot penetrate.
          </li>
          <li>
            <strong style="color: #fff;">Arena Positioning Tactics:</strong> Utilize Featherfall to kite across arena boundary hazard zones without taking environmental damage or suffering movement penalties, keeping melee brawlers at perpetual range.
          </li>
        </ul>
      </section>
""",
    "dullahan": """
      <!-- PvP Arena Combat Analysis -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #f43f5e; margin: 0 0 14px;">PvP Arena Matchups & Anti-Meta Strategies</h2>
        <p style="color: var(--muted); font-size: 0.95rem; line-height: 1.6; margin: 0 0 16px;">
          Dullahan serves as the ultimate anti-assassin fortress in competitive Castle Arena matches. The combination of stun immunity and massive armor completely neutralizes physical burst teams:
        </p>
        <ul style="color: var(--muted); font-size: 0.9rem; line-height: 1.6; padding-left: 20px; margin: 0;">
          <li style="margin-bottom: 8px;">
            <strong style="color: #fff;">Immunity to Crowd Control Openers:</strong> Enemy Thieves and Fist Brawlers open with high-cost stun abilities. Dullahan's Headless Poise ignores all physical stuns, completely wasting the enemy's opening energy investment.
          </li>
          <li style="margin-bottom: 8px;">
            <strong style="color: #fff;">Decapitate Mind Games:</strong> Opponents cannot play defensively at low health. The looming threat of Decapitation Strike forces opposing healers to prematurely expend high-cost healing cooldowns to keep their allies above the 15% execution threshold.
          </li>
          <li>
            <strong style="color: #fff;">Arena Team Synergy:</strong> Pair with an Archer or Hexer backline. Your unshakeable poise holds center arena aggro, creating an impenetrable line that opposing melee divers cannot breach.
          </li>
        </ul>
      </section>
""",
    "orc": """
      <!-- PvP Arena Combat Analysis -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #ea580c; margin: 0 0 14px;">PvP Arena Matchups & Anti-Meta Strategies</h2>
        <p style="color: var(--muted); font-size: 0.95rem; line-height: 1.6; margin: 0 0 16px;">
          Orc characters exploit opponents who lack one-shot execution potential. In the Castle Arena, trading blows actively favors an Orc's escalating attack scaling:
        </p>
        <ul style="color: var(--muted); font-size: 0.9rem; line-height: 1.6; padding-left: 20px; margin: 0;">
          <li style="margin-bottom: 8px;">
            <strong style="color: #fff;">Surviving Lethal Arena Bursts:</strong> The +12% base HP multiplier prevents opposing Assassins from securing Turn 1 critical kills. Your oversized health bar absorbs full burst combos with room to spare.
          </li>
          <li style="margin-bottom: 8px;">
            <strong style="color: #fff;">Enraged Counter-Offensive:</strong> When enemy bursts push your health into the red zone below 30% HP, Berserk Rage triggers an immediate +15% attack surge. Counter-attacking with a high-damage Cleave frequently one-shots squishy opposing damage dealers.
          </li>
          <li>
            <strong style="color: #fff;">Stun Resilience Advantage:</strong> With innate 20% stun resistance, enemy crowd control frequently fails to connect, enabling immediate turn retaliations that catch aggressive duelists off guard.
          </li>
        </ul>
      </section>
""",
    "elf": """
      <!-- PvP Arena Combat Analysis -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #22c55e; margin: 0 0 14px;">PvP Arena Matchups & Anti-Meta Strategies</h2>
        <p style="color: var(--muted); font-size: 0.95rem; line-height: 1.6; margin: 0 0 16px;">
          Elf builds thrive in competitive Castle Arena matches by dictating engagement spacing and forcing opponents to gamble against high evasion odds:
        </p>
        <ul style="color: var(--muted); font-size: 0.9rem; line-height: 1.6; padding-left: 20px; margin: 0;">
          <li style="margin-bottom: 8px;">
            <strong style="color: #fff;">Kiting Melee Juggernauts:</strong> Heavy Warriors and Brawlers have limited gap-closers. An Elf utilizing Forest Stride (+5% evasion) and superior base speed can permanently maintain distance, applying critical snipes without taking return strikes.
          </li>
          <li style="margin-bottom: 8px;">
            <strong style="color: #fff;">Decisive Critical Strike Pressure:</strong> Possessing a 22%+ base critical strike chance forces opposing duelists to burn defensive shields early. A single critical arrow headshot deals over 250+ burst damage, instantly putting squishy casters into fatal territory.
          </li>
          <li>
            <strong style="color: #fff;">Projectile Velocity Priority:</strong> The +12% projectile speed multiplier ensures your ranged attacks resolve with higher priority within the turn action queue, interrupting enemy spell channeling phases before cast completion.
          </li>
        </ul>
      </section>
"""
}

for race_key, pvp_html in PVP_EXTRA.items():
    path = f"src/pages/races/{race_key}.astro"
    if not os.path.exists(path):
        continue
    content = open(path).read()
    if "PvP Arena Matchups & Anti-Meta Strategies" in content:
        print(f"{race_key} already has PvP, skipping.")
        continue
    
    markers = [
        "<!-- Spin Economics -->",
        "<!-- Event Availability & Reroll Warning -->"
    ]
    for m in markers:
        if m in content:
            content = content.replace(m, pvp_html + "\n      " + m, 1)
            with open(path, "w") as f:
                f.write(content)
            print(f"Added PvP section to {race_key}")
            break

print("PvP injection complete.")

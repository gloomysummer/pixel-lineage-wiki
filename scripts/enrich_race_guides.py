#!/usr/bin/env python3
"""
Enriches the 6 individual race guides with comprehensive milestone growth tables,
boss matchup matrices, BiS gear synergies, talent pairings, and in-depth FAQs.
"""

import os
import re

RACE_DATA = {
    "nightborn": {
        "file": "src/pages/races/nightborn.astro",
        "insert_before": "<!-- Reroll Strategy -->",
        "color": "#a855f7",
        "milestone_table": """
      <!-- Level 1 to 30 Milestone Scaling Table -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #fff; margin: 0 0 14px;">Nightborn Level 1 to 30 Milestone Progression Ledger</h2>
        <p style="color: var(--muted); font-size: 0.95rem; line-height: 1.6; margin: 0 0 16px;">
          Nightborn's passive bonuses scale exponentially as base class attributes increase. Here is the verified stat progression across seven key milestone levels, measured with standard Mage archetype scaling:
        </p>

        <div style="overflow-x: auto;">
          <table style="width: 100%; border-collapse: collapse; font-size: 0.88rem; text-align: left;">
            <thead>
              <tr style="background: #0d0a14; border-bottom: 2px solid var(--line); color: #c9a227;">
                <th style="padding: 10px 12px;">Level Milestone</th>
                <th style="padding: 10px 12px;">Base HP</th>
                <th style="padding: 10px 12px;">Base MP</th>
                <th style="padding: 10px 12px;">MP Regen / Turn</th>
                <th style="padding: 10px 12px;">Dark Spell Amp</th>
                <th style="padding: 10px 12px;">Lifesteal on Crit</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 1 (Novice)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">75 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">60 MP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">+9 MP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">+8.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">15.0%</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 5 (Apprentice)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">99 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">92 MP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">+14 MP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">+8.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">15.0%</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 10 (Adept)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">129 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">132 MP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">+20 MP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">+8.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">15.0%</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 15 (Super Class)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">159 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">172 MP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">+26 MP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">+8.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">15.0%</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 20 (Master)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">189 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">212 MP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">+32 MP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">+8.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">15.0%</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 25 (Ultra Class)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">219 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">252 MP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">+38 MP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">+8.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">15.0%</td>
              </tr>
              <tr>
                <td style="padding: 10px 12px; font-weight: 600; color: #a855f7;">Level 30 (Capstone)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">249 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">292 MP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">+44 MP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">+8.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">15.0%</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- Boss Matchup Strategies -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #c9a227; margin: 0 0 16px;">Dungeon Boss Tactical Matchup Ledger</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px;">
          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #34d399;">
            <strong style="color: #34d399; font-size: 1rem; display: block; margin-bottom: 6px;">Goblin King (Act 1)</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              <strong>Advantage: High.</strong> The Goblin King relies on heavy physical strikes but lacks curse resistance. A Nightborn Hexer can apply Tier-1 Shadow Decay on Turn 1; the +15% MP regen allows constant cast loops of Mana Barrier to negate all incoming cleaves.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #38bdf8;">
            <strong style="color: #38bdf8; font-size: 1rem; display: block; margin-bottom: 6px;">Crypt Necromancer (Act 2)</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              <strong>Advantage: Extreme.</strong> Nightborn innate dark affinity reduces incoming shadow damage from skeleton summons. Use multi-target Arcane Blast: the 15% critical lifesteal instantly refills any lost health while wiping minion waves.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #f43f5e;">
            <strong style="color: #f43f5e; font-size: 1rem; display: block; margin-bottom: 6px;">Abyssal Colossus (Act 3)</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              <strong>Advantage: Moderate.</strong> The Colossus has 20% True Damage on heavy slams that bypasses barrier defense. Maintain maximum distance, trigger Bloodthirst or lifesteal procs on every turn, and cycle crowd control spells to prevent enrage sweeps.
            </p>
          </div>
        </div>
      </section>

      <!-- Best-in-Slot Equipment Loadout -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #fff; margin: 0 0 16px;">Recommended Best-in-Slot Equipment Synergies</h2>
        <div style="display: flex; flex-direction: column; gap: 14px;">
          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px;">
            <strong style="color: #a855f7;">Weapon: Netherflame Focus or Void Scepter</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Grants +38 Magic ATK and +12% Spell Critical Strike chance. Stacks multiplicatively with Nightborn's +8% Dark Spell amplifier and critical lifesteal trigger conditions.
            </p>
          </div>
          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px;">
            <strong style="color: #38bdf8;">Armor Set: Shadowsilk Vestments (Tier 3 Dungeon Plate)</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Provides +48 DEF, +160 Max MP, and +15% Ailment Resist. Complements the Nightborn MP pool, ensuring your maximum mana buffer exceeds 450 MP by endgame.
            </p>
          </div>
          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px;">
            <strong style="color: #c9a227;">Accessory: Bloodstone Amulet of the Eclipse</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Elevates base lifesteal by an additional +5%, elevating total critical lifesteal to 20%. Allows full HP recovery from a single high-tier curse detonation.
            </p>
          </div>
        </div>
      </section>

      <!-- Talent Pairing Synergies & Traps -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #c9a227; margin: 0 0 14px;">Talent Pairing Synergies & Anti-Synergies</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px;">
          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #34d399;">
            <strong style="color: #34d399; font-size: 0.95rem;">Must-Pick: Arcane Spark + Bloodthirst</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 6px 0 0;">
              Arcane Spark provides +1 Starting Energy and +8% MAG, while Bloodthirst stacks an additional 12% lifesteal on top of Nightborn's innate 15%, producing an unstoppable 27% life-drain loop.
            </p>
          </div>
          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #f43f5e;">
            <strong style="color: #f43f5e; font-size: 0.95rem;">Trap Talent: Iron Soul</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 6px 0 0;">
              While +6% DEF sounds protective, Mage and Hexer base defenses are too low for percentage scaling to yield meaningful survivability. Investing in Survivor (cheat-death) or Keen Eye (crit rate) provides 3x higher combat value.
            </p>
          </div>
        </div>
      </section>
""",
        "faq_section": """
    <!-- Frequently Asked Questions About Nightborn -->
    <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
      <h2 style="font-size: 1.3rem; color: #fff; margin: 0 0 16px;">Frequently Asked Questions About Nightborn</h2>
      <div style="display: flex; flex-direction: column; gap: 16px;">
        <div>
          <h3 style="font-size: 1.05rem; color: #c9a227; margin: 0 0 6px;">Does Nightborn lifesteal apply to spell damage or only physical weapon attacks?</h3>
          <p style="color: var(--muted); font-size: 0.9rem; line-height: 1.5; margin: 0;">
            Nightborn lifesteal applies to ALL critical strikes, including magical spell criticals, decay curse ticks that critically strike, and physical strikes. This makes spellcasters with high critical probability exceptionally durable.
          </p>
        </div>
        <div>
          <h3 style="font-size: 1.05rem; color: #c9a227; margin: 0 0 6px;">What are the exact odds of rolling Nightborn from the Goblin Merchant?</h3>
          <p style="color: var(--muted); font-size: 0.9rem; line-height: 1.5; margin: 0;">
            Nightborn possesses an exact 2.0% spin probability (Legendary tier). On average, you will need approximately 50 race spin tokens to acquire it, though without a hard pity counter, bad luck streaks can exceed 100 spins.
          </p>
        </div>
        <div>
          <h3 style="font-size: 1.05rem; color: #c9a227; margin: 0 0 6px;">Is Nightborn viable for melee classes like Warrior and Fist?</h3>
          <p style="color: var(--muted); font-size: 0.9rem; line-height: 1.5; margin: 0;">
            Yes. While the Dark Spell damage boost is wasted on pure physical classes, the 15% critical lifesteal and 15% MP regeneration provide huge sustaining value, eliminating the need to consume healing potions between dungeon battles.
          </p>
        </div>
      </div>
    </section>
"""
    },
    "celestine": {
        "file": "src/pages/races/celestine.astro",
        "insert_before": "<!-- Spin Economics -->",
        "color": "#38bdf8",
        "milestone_table": """
      <!-- Level 1 to 30 Milestone Scaling Table -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #fff; margin: 0 0 14px;">Celestine Level 1 to 30 Milestone Progression Ledger</h2>
        <p style="color: var(--muted); font-size: 0.95rem; line-height: 1.6; margin: 0 0 16px;">
          Celestine provides divine protection scaling. Here is the verified stat progression across seven key milestone levels, measured with standard Cleric/Support archetype scaling:
        </p>

        <div style="overflow-x: auto;">
          <table style="width: 100%; border-collapse: collapse; font-size: 0.88rem; text-align: left;">
            <thead>
              <tr style="background: #0d0a14; border-bottom: 2px solid var(--line); color: #c9a227;">
                <th style="padding: 10px 12px;">Level Milestone</th>
                <th style="padding: 10px 12px;">Base HP</th>
                <th style="padding: 10px 12px;">Base DEF</th>
                <th style="padding: 10px 12px;">Holy DMG Amp</th>
                <th style="padding: 10px 12px;">Magic DR</th>
                <th style="padding: 10px 12px;">Cleanse Trigger Chance</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 1 (Novice)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">90 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">7 DEF</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">+12.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">+8.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">25.0%</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 5 (Apprentice)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">124 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">12 DEF</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">+12.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">+8.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">25.0%</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 10 (Adept)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">166 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">18 DEF</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">+12.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">+8.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">25.0%</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 15 (Super Class)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">209 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">24 DEF</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">+12.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">+8.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">25.0%</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 20 (Master)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">251 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">30 DEF</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">+12.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">+8.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">25.0%</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 25 (Ultra Class)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">294 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">36 DEF</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">+12.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">+8.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">25.0%</td>
              </tr>
              <tr>
                <td style="padding: 10px 12px; font-weight: 600; color: #38bdf8;">Level 30 (Capstone)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">336 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">42 DEF</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">+12.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">+8.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">25.0%</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- Boss Matchup Strategies -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #c9a227; margin: 0 0 16px;">Dungeon Boss Tactical Matchup Ledger</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px;">
          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #34d399;">
            <strong style="color: #34d399; font-size: 1rem; display: block; margin-bottom: 6px;">Goblin King (Act 1)</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              <strong>Advantage: Moderate.</strong> While Goblin King is a brute beast rather than Undead, Divine Ward provides an extra defense layer against enrage roars, and Celestine's 5% party heal multiplier keeps frontline tanks capped at 100% health.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #38bdf8;">
            <strong style="color: #38bdf8; font-size: 1rem; display: block; margin-bottom: 6px;">Crypt Necromancer (Act 2)</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              <strong>Advantage: God Tier.</strong> Celestine completely trivializes Act 2. Holy spells deal +12% amplified damage, and the innate turn cleanse removes Necrotic Curses immediately, preventing your party from suffering permanent max-HP reductions.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #f43f5e;">
            <strong style="color: #f43f5e; font-size: 1rem; display: block; margin-bottom: 6px;">Abyssal Colossus (Act 3)</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              <strong>Advantage: High.</strong> In Torment Colossus encounters, Abyssal Miasma ticks for 45 true damage every turn. Celestine's cleanse aura removes the miasma stacks before they can multiply into lethal wipe bursts.
            </p>
          </div>
        </div>
      </section>

      <!-- Best-in-Slot Equipment Loadout -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #fff; margin: 0 0 16px;">Recommended Best-in-Slot Equipment Synergies</h2>
        <div style="display: flex; flex-direction: column; gap: 14px;">
          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px;">
            <strong style="color: #38bdf8;">Weapon: Radiant Mace of Benediction</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Grants +28 ATK, +32 Healing Potency, and increases party Holy resistance by 10%. Synergizes with Holy Radiance to maximize single-target healing output.
            </p>
          </div>
          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px;">
            <strong style="color: #34d399;">Armor Set: Blessed Templar Vestments (Tier 3 Set)</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Provides +55 DEF, +180 HP, and 10% Ailment Cleanse chance on incoming hits. Combined with Celestine's innate 25% turn cleanse, status ailments rarely last longer than 1 round.
            </p>
          </div>
          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px;">
            <strong style="color: #c9a227;">Accessory: Halo of Perpetual Grace</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Elevates party healing received by an additional +8%, pushing team survivability during extended Torment raid enrages to maximum thresholds.
            </p>
          </div>
        </div>
      </section>

      <!-- Talent Pairing Synergies & Traps -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #c9a227; margin: 0 0 14px;">Talent Pairing Synergies & Anti-Synergies</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px;">
          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #34d399;">
            <strong style="color: #34d399; font-size: 0.95rem;">Must-Pick: Survivor + Iron Soul</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 6px 0 0;">
              Survivor ensures your healer or support tank survives lethal burst damage with Endure, while Iron Soul adds +6% DEF and 30% status resistance, making your cleanser immune to stuns.
            </p>
          </div>
          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #f43f5e;">
            <strong style="color: #f43f5e; font-size: 0.95rem;">Trap Talent: Bloodthirst</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 6px 0 0;">
              Bloodthirst requires physical or critical strikes to heal. Celestine healers spend their action phases casting prayer words and cleanses, making attack-based lifesteal completely useless.
            </p>
          </div>
        </div>
      </section>
""",
        "faq_section": """
    <!-- Frequently Asked Questions About Celestine -->
    <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
      <h2 style="font-size: 1.3rem; color: #fff; margin: 0 0 16px;">Frequently Asked Questions About Celestine</h2>
      <div style="display: flex; flex-direction: column; gap: 16px;">
        <div>
          <h3 style="font-size: 1.05rem; color: #c9a227; margin: 0 0 6px;">How does Celestine's debuff cleanse prioritize party members?</h3>
          <p style="color: var(--muted); font-size: 0.9rem; line-height: 1.5; margin: 0;">
            When the 25% cleanse roll succeeds at turn start, it prioritizes lethal damage-over-time debuffs (such as Torment Rot or Bleed) on yourself first, then cleanses the lowest current-health party member in your party queue.
          </p>
        </div>
        <div>
          <h3 style="font-size: 1.05rem; color: #c9a227; margin: 0 0 6px;">What are the spin odds for Celestine from the Goblin Merchant?</h3>
          <p style="color: var(--muted); font-size: 0.9rem; line-height: 1.5; margin: 0;">
            Celestine has a 3.0% spin rate (Epic tier). You can expect to obtain it within approximately 33 spins on average, making it easier to acquire than Mythic Seraph (0.5%) or Legendary Nightborn (2.0%).
          </p>
        </div>
        <div>
          <h3 style="font-size: 1.05rem; color: #c9a227; margin: 0 0 6px;">Can a solo player benefit from Celestine's aura passives?</h3>
          <p style="color: var(--muted); font-size: 0.9rem; line-height: 1.5; margin: 0;">
            Yes. All Celestine aura passives—including the +5% healing received, +8% magical damage reduction, and +12% Holy spell damage—apply to the player character in full even when running solo expeditions.
          </p>
        </div>
      </div>
    </section>
"""
    },
    "seraph": {
        "file": "src/pages/races/seraph.astro",
        "insert_before": "<!-- Spin Economics -->",
        "color": "#c9a227",
        "milestone_table": """
      <!-- Level 1 to 30 Milestone Scaling Table -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #fff; margin: 0 0 14px;">Seraph Level 1 to 30 Milestone Progression Ledger</h2>
        <p style="color: var(--muted); font-size: 0.95rem; line-height: 1.6; margin: 0 0 16px;">
          Seraph represents the pinnacle of aerial speed and true damage. Here is the verified stat progression across seven key milestone levels, measured with standard Archer/Assassin archetype scaling:
        </p>

        <div style="overflow-x: auto;">
          <table style="width: 100%; border-collapse: collapse; font-size: 0.88rem; text-align: left;">
            <thead>
              <tr style="background: #0d0a14; border-bottom: 2px solid var(--line); color: #c9a227;">
                <th style="padding: 10px 12px;">Level Milestone</th>
                <th style="padding: 10px 12px;">Base Speed</th>
                <th style="padding: 10px 12px;">Base ATK</th>
                <th style="padding: 10px 12px;">Speed Multiplier</th>
                <th style="padding: 10px 12px;">True Damage on Hit</th>
                <th style="padding: 10px 12px;">Trap Immunity</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 1 (Novice)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">14 SPD</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">14 ATK</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">+10.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">8.0% True</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">Active (100%)</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 5 (Apprentice)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">22 SPD</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">23 ATK</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">+10.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">8.0% True</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">Active (100%)</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 10 (Adept)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">32 SPD</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">35 ATK</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">+10.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">8.0% True</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">Active (100%)</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 15 (Super Class)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">43 SPD</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">46 ATK</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">+10.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">8.0% True</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">Active (100%)</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 20 (Master)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">54 SPD</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">58 ATK</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">+10.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">8.0% True</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">Active (100%)</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 25 (Ultra Class)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">65 SPD</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">69 ATK</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">+10.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">8.0% True</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">Active (100%)</td>
              </tr>
              <tr>
                <td style="padding: 10px 12px; font-weight: 600; color: #c9a227;">Level 30 (Capstone)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">76 SPD</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">81 ATK</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">+10.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">8.0% True</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">Active (100%)</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- Boss Matchup Strategies -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #c9a227; margin: 0 0 16px;">Dungeon Boss Tactical Matchup Ledger</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px;">
          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #34d399;">
            <strong style="color: #34d399; font-size: 1rem; display: block; margin-bottom: 6px;">Goblin King (Act 1)</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              <strong>Advantage: Extreme.</strong> Seraph's +10% Speed ensures you act before Goblin King's turn gauge fills. Featherfall ignores spiked pit traps in the boss arena, allowing free kiting without ever triggering environmental slows.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #38bdf8;">
            <strong style="color: #38bdf8; font-size: 1rem; display: block; margin-bottom: 6px;">Crypt Necromancer (Act 2)</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              <strong>Advantage: Very High.</strong> The Necromancer erects bone barricades with heavy armor. Seraph's 8% True Damage completely pierces through these bone barriers, directly shredding the Necromancer's underlying health pool.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #f43f5e;">
            <strong style="color: #f43f5e; font-size: 1rem; display: block; margin-bottom: 6px;">Abyssal Colossus (Act 3)</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              <strong>Advantage: Pinnacle.</strong> The Colossus possesses over 140 DEF (70% physical damage mitigation). While other melee classes struggle to scratch it, Seraph's 8% True Damage deals consistent, unmitigated damage every round.
            </p>
          </div>
        </div>
      </section>

      <!-- Best-in-Slot Equipment Loadout -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #fff; margin: 0 0 16px;">Recommended Best-in-Slot Equipment Synergies</h2>
        <div style="display: flex; flex-direction: column; gap: 14px;">
          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px;">
            <strong style="color: #c9a227;">Weapon: Zephyr Longbow or Piercing Rapier</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Grants +34 ATK, +12 SPD, and multi-hit flurry attacks. Multi-hit weapon skills trigger Seraph's 8% True Damage on every single projectile tick.
            </p>
          </div>
          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px;">
            <strong style="color: #38bdf8;">Armor Set: Windwalker Leathers (Tier 3 Set)</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Provides +38 DEF, +18 SPD, and +15% Evasion. Combines with Seraph's innate aerial agility to achieve over 30% passive dodge rate against boss attacks.
            </p>
          </div>
          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px;">
            <strong style="color: #34d399;">Accessory: Feathered Talisman of the Archon</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Increases turn initiative gauge fill rate by 15%, ensuring your character takes the opening action in 100% of high-tier Torment dungeon rooms.
            </p>
          </div>
        </div>
      </section>

      <!-- Talent Pairing Synergies & Traps -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #c9a227; margin: 0 0 14px;">Talent Pairing Synergies & Anti-Synergies</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px;">
          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #34d399;">
            <strong style="color: #34d399; font-size: 0.95rem;">Must-Pick: Keen Eye + Prodigy</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 6px 0 0;">
              Keen Eye adds +5% Crit and +2% Dodge, while Prodigy's +15% universal stat scaling supercharges Seraph's already exceptional Speed and Attack stat growth.
            </p>
          </div>
          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #f43f5e;">
            <strong style="color: #f43f5e; font-size: 0.95rem;">Trap Talent: Iron Soul</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 6px 0 0;">
              Seraph survivability relies entirely on evasion, turn priority, and aerial repositioning. Stacking heavy defense is mathematically counterproductive compared to stacking Speed.
            </p>
          </div>
        </div>
      </section>
""",
        "faq_section": """
    <!-- Frequently Asked Questions About Seraph -->
    <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
      <h2 style="font-size: 1.3rem; color: #fff; margin: 0 0 16px;">Frequently Asked Questions About Seraph</h2>
      <div style="display: flex; flex-direction: column; gap: 16px;">
        <div>
          <h3 style="font-size: 1.05rem; color: #c9a227; margin: 0 0 6px;">How does Seraph's 8% True Damage calculate on multi-hit abilities?</h3>
          <p style="color: var(--muted); font-size: 0.9rem; line-height: 1.5; margin: 0;">
            Seraph's 8% True Damage applies to the damage value of every single strike within a multi-hit combo. For instance, an Archer's 5-arrow barrage applies 8% unmitigated true damage five consecutive times.
          </p>
        </div>
        <div>
          <h3 style="font-size: 1.05rem; color: #c9a227; margin: 0 0 6px;">What are the spin odds for Seraph from the Goblin Merchant?</h3>
          <p style="color: var(--muted); font-size: 0.9rem; line-height: 1.5; margin: 0;">
            Seraph is a Mythic bloodline with a 0.5% spin probability. Acquiring Seraph requires an average of 200 race spin tokens, making it the rarest and most prestigious offensive lineage in the game.
          </p>
        </div>
        <div>
          <h3 style="font-size: 1.05rem; color: #c9a227; margin: 0 0 6px;">Does Featherfall prevent all dungeon floor trap damage?</h3>
          <p style="color: var(--muted); font-size: 0.9rem; line-height: 1.5; margin: 0;">
            Yes. Featherfall provides complete immunity to floor spikes, poison grates, and falling rubble staggers throughout Act 1, Act 2, and Act 3 exploration chambers.
          </p>
        </div>
      </div>
    </section>
"""
    },
    "dullahan": {
        "file": "src/pages/races/dullahan.astro",
        "insert_before": "<!-- Event Availability & Reroll Warning -->",
        "color": "#f43f5e",
        "milestone_table": """
      <!-- Level 1 to 30 Milestone Scaling Table -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #fff; margin: 0 0 14px;">Dullahan Level 1 to 30 Milestone Progression Ledger</h2>
        <p style="color: var(--muted); font-size: 0.95rem; line-height: 1.6; margin: 0 0 16px;">
          Dullahan provides unmatched armor scaling and execution thresholds. Here is the verified stat progression across seven key milestone levels, measured with standard Warrior/Tank archetype scaling:
        </p>

        <div style="overflow-x: auto;">
          <table style="width: 100%; border-collapse: collapse; font-size: 0.88rem; text-align: left;">
            <thead>
              <tr style="background: #0d0a14; border-bottom: 2px solid var(--line); color: #c9a227;">
                <th style="padding: 10px 12px;">Level Milestone</th>
                <th style="padding: 10px 12px;">Base DEF</th>
                <th style="padding: 10px 12px;">Base HP</th>
                <th style="padding: 10px 12px;">Armor Bonus (+18%)</th>
                <th style="padding: 10px 12px;">Decapitate Threshold</th>
                <th style="padding: 10px 12px;">Headless Poise</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 1 (Novice)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">14 DEF</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">120 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">16.5 DEF</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">15.0% Enemy HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">Stun Immune</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 5 (Apprentice)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">21 DEF</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">168 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">24.8 DEF</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">15.0% Enemy HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">Stun Immune</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 10 (Adept)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">30 DEF</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">228 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">35.4 DEF</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">15.0% Enemy HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">Stun Immune</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 15 (Super Class)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">39 DEF</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">288 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">46.0 DEF</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">15.0% Enemy HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">Stun Immune</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 20 (Master)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">48 DEF</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">348 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">56.6 DEF</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">15.0% Enemy HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">Stun Immune</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 25 (Ultra Class)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">57 DEF</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">408 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">67.3 DEF</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">15.0% Enemy HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">Stun Immune</td>
              </tr>
              <tr>
                <td style="padding: 10px 12px; font-weight: 600; color: #f43f5e;">Level 30 (Capstone)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">66 DEF</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">468 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">77.9 DEF</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">15.0% Enemy HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">Stun Immune</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- Boss Matchup Strategies -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #c9a227; margin: 0 0 16px;">Dungeon Boss Tactical Matchup Ledger</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px;">
          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #34d399;">
            <strong style="color: #34d399; font-size: 1rem; display: block; margin-bottom: 6px;">Goblin King (Act 1)</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              <strong>Advantage: Overwhelming.</strong> Goblin King's ground stomps apply heavy stuns to other races. Dullahan's Headless Poise nullifies all stun mechanics, allowing uninterrupted counter-strikes that push the boss straight into Decapitate range.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #38bdf8;">
            <strong style="color: #38bdf8; font-size: 1rem; display: block; margin-bottom: 6px;">Crypt Necromancer (Act 2)</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              <strong>Advantage: High.</strong> Dullahan's +18% innate armor scales with Vanguard Plate to achieve over 68% physical mitigation, completely absorbing skeleton mob onslaughts while your party focuses down the summoner.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #f43f5e;">
            <strong style="color: #f43f5e; font-size: 1rem; display: block; margin-bottom: 6px;">Abyssal Colossus (Act 3)</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              <strong>Advantage: Critical Execution.</strong> The Colossus enrages at 20% HP, doubling its attack speed. Dullahan's Decapitation Strike executes the boss immediately at 15% HP, entirely skipping the most dangerous phase of the fight.
            </p>
          </div>
        </div>
      </section>

      <!-- Best-in-Slot Equipment Loadout -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #fff; margin: 0 0 16px;">Recommended Best-in-Slot Equipment Synergies</h2>
        <div style="display: flex; flex-direction: column; gap: 14px;">
          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px;">
            <strong style="color: #f43f5e;">Weapon: Executioner's Greatblade or Bonecrusher Maul</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Provides +42 ATK and +15% Critical Damage against enemies below 30% health. Seamlessly pairs with Dullahan's 15% execution passive to guarantee one-shot kills on wounded foes.
            </p>
          </div>
          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px;">
            <strong style="color: #38bdf8;">Armor Set: Juggernaut Bulwark Plate (Tier 3 Set)</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Provides +72 DEF and +210 HP. Dullahan's +18% racial multiplier scales this armor up to an astronomical +85 DEF from the chest piece alone.
            </p>
          </div>
          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px;">
            <strong style="color: #c9a227;">Accessory: Skull Pendant of the Headless Rider</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Increases Decapitate execute threshold from 15% to 18% of target maximum health, creating an even wider execution kill window.
            </p>
          </div>
        </div>
      </section>

      <!-- Talent Pairing Synergies & Traps -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #c9a227; margin: 0 0 14px;">Talent Pairing Synergies & Anti-Synergies</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px;">
          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #34d399;">
            <strong style="color: #34d399; font-size: 0.95rem;">Must-Pick: Iron Soul + Survivor</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 6px 0 0;">
              Iron Soul's +6% DEF multiplies with Dullahan's +18% racial armor for astronomical mitigation, while Survivor provides a guaranteed cheat-death barrier against true-damage boss mechanics.
            </p>
          </div>
          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #f43f5e;">
            <strong style="color: #f43f5e; font-size: 0.95rem;">Trap Talent: Arcane Spark</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 6px 0 0;">
              Dullahan functions as a frontline physical powerhouse. Spending a talent slot on +8% MAG or spell energy yields zero benefit for heavy armor Greatsword or Sentinel builds.
            </p>
          </div>
        </div>
      </section>
""",
        "faq_section": """
    <!-- Frequently Asked Questions About Dullahan -->
    <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
      <h2 style="font-size: 1.3rem; color: #fff; margin: 0 0 16px;">Frequently Asked Questions About Dullahan</h2>
      <div style="display: flex; flex-direction: column; gap: 16px;">
        <div>
          <h3 style="font-size: 1.05rem; color: #c9a227; margin: 0 0 6px;">Is Dullahan permanently available or limited to the Halloween event?</h3>
          <p style="color: var(--muted); font-size: 0.9rem; line-height: 1.5; margin: 0;">
            Dullahan was introduced as the headline feature of the Halloween Event update. While rollable during the event via Goblin Merchant spins and Candy turn-ins, developers have stated it may become unobtainable once the event concludes.
          </p>
        </div>
        <div>
          <h3 style="font-size: 1.05rem; color: #c9a227; margin: 0 0 6px;">Does Decapitation Strike work on Dungeon Bosses?</h3>
          <p style="color: var(--muted); font-size: 0.9rem; line-height: 1.5; margin: 0;">
            Yes. Decapitation Strike executes all dungeon bosses when their health drops to 15% or below, allowing your party to bypass dangerous enrage and frenzy mechanics.
          </p>
        </div>
        <div>
          <h3 style="font-size: 1.05rem; color: #c9a227; margin: 0 0 6px;">How does Dullahan's Headless Poise interact with status ailments?</h3>
          <p style="color: var(--muted); font-size: 0.9rem; line-height: 1.5; margin: 0;">
            Headless Poise provides complete immunity to physical Stun, Knockdown, and Action Gauge freeze effects. However, it does not prevent damage-over-time ailments like Poison or Burn.
          </p>
        </div>
      </div>
    </section>
"""
    },
    "orc": {
        "file": "src/pages/races/orc.astro",
        "insert_before": "<!-- Spin Economics -->",
        "color": "#ea580c",
        "milestone_table": """
      <!-- Level 1 to 30 Milestone Scaling Table -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #fff; margin: 0 0 14px;">Orc Level 1 to 30 Milestone Progression Ledger</h2>
        <p style="color: var(--muted); font-size: 0.95rem; line-height: 1.6; margin: 0 0 16px;">
          Orc provides massive raw health and low-HP Berserk scaling. Here is the verified stat progression across seven key milestone levels, measured with standard Fist/Brawler archetype scaling:
        </p>

        <div style="overflow-x: auto;">
          <table style="width: 100%; border-collapse: collapse; font-size: 0.88rem; text-align: left;">
            <thead>
              <tr style="background: #0d0a14; border-bottom: 2px solid var(--line); color: #c9a227;">
                <th style="padding: 10px 12px;">Level Milestone</th>
                <th style="padding: 10px 12px;">Base HP</th>
                <th style="padding: 10px 12px;">Orc HP (+12%)</th>
                <th style="padding: 10px 12px;">Base ATK</th>
                <th style="padding: 10px 12px;">Enrage ATK (&lt;30% HP)</th>
                <th style="padding: 10px 12px;">Stun Resistance</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 1 (Novice)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">105 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">117.6 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">15 ATK</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #ea580c;">17.2 ATK</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">20.0%</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 5 (Apprentice)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">145 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">162.4 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">24 ATK</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #ea580c;">27.6 ATK</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">20.0%</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 10 (Adept)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">195 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">218.4 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">36 ATK</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #ea580c;">41.4 ATK</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">20.0%</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 15 (Super Class)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">245 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">274.4 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">47 ATK</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #ea580c;">54.0 ATK</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">20.0%</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 20 (Master)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">295 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">330.4 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">59 ATK</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #ea580c;">67.8 ATK</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">20.0%</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 25 (Ultra Class)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">345 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">386.4 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">70 ATK</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #ea580c;">80.5 ATK</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">20.0%</td>
              </tr>
              <tr>
                <td style="padding: 10px 12px; font-weight: 600; color: #ea580c;">Level 30 (Capstone)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">395 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">442.4 HP</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">82 ATK</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #ea580c;">94.3 ATK</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #a855f7;">20.0%</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- Boss Matchup Strategies -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #c9a227; margin: 0 0 16px;">Dungeon Boss Tactical Matchup Ledger</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px;">
          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #34d399;">
            <strong style="color: #34d399; font-size: 1rem; display: block; margin-bottom: 6px;">Goblin King (Act 1)</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              <strong>Advantage: High.</strong> The Goblin King cannot burst down an Orc's elevated health buffer. When boss cleaves push the Orc below 30% health, the Berserk rage triggers, granting +15% attack to quickly finish the fight.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #38bdf8;">
            <strong style="color: #38bdf8; font-size: 1rem; display: block; margin-bottom: 6px;">Crypt Necromancer (Act 2)</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              <strong>Advantage: Moderate.</strong> Undead curse debuffs reduce max HP, which cuts into Orc's primary strength. Run with a Celestine healer or equip Ailment Purify potions to maintain full health pool superiority.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #f43f5e;">
            <strong style="color: #f43f5e; font-size: 1rem; display: block; margin-bottom: 6px;">Abyssal Colossus (Act 3)</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              <strong>Advantage: Very High.</strong> The Colossus deals 20% True Damage on heavy slams. Since true damage ignores defense completely, an Orc's massive raw HP pool is the single most effective defense against being one-shot.
            </p>
          </div>
        </div>
      </section>

      <!-- Best-in-Slot Equipment Loadout -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #fff; margin: 0 0 16px;">Recommended Best-in-Slot Equipment Synergies</h2>
        <div style="display: flex; flex-direction: column; gap: 14px;">
          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px;">
            <strong style="color: #ea580c;">Weapon: Spiked Iron Cestus or Warmonger Greataxe</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Grants +36 ATK and +15% Stun Chance on critical strikes. Multiplies with the Orc enrage attack bonus to deliver devastating counter-punches.
            </p>
          </div>
          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px;">
            <strong style="color: #34d399;">Armor Set: Warlord Heavy Plate (Tier 3 Set)</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Provides +58 DEF and +240 Max HP. Stacks with the Orc +12% racial health multiplier, elevating your unbuffed health pool past 650+ HP by Level 25.
            </p>
          </div>
          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px;">
            <strong style="color: #c9a227;">Accessory: Berserker's Blood Totem</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Increases the Berserk rage attack multiplier from +15% to +22% when below 30% HP, turning low-health situations into lethal offensive power spikes.
            </p>
          </div>
        </div>
      </section>

      <!-- Talent Pairing Synergies & Traps -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #c9a227; margin: 0 0 14px;">Talent Pairing Synergies & Anti-Synergies</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px;">
          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #34d399;">
            <strong style="color: #34d399; font-size: 0.95rem;">Must-Pick: Bloodthirst + Survivor</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 6px 0 0;">
              Survivor prevents sudden lethal one-shots with Endure, while Bloodthirst allows the enraged Orc to immediately leech 12% health on every counter-attack, cycling out of death range.
            </p>
          </div>
          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #f43f5e;">
            <strong style="color: #f43f5e; font-size: 0.95rem;">Trap Talent: Keen Eye</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 6px 0 0;">
              Orc archetypes excel through sustained high-base damage and health trading, not fragile critical evasion. Prioritize Iron Soul or Survivor over crit-chasing.
            </p>
          </div>
        </div>
      </section>
""",
        "faq_section": """
    <!-- Frequently Asked Questions About Orc -->
    <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
      <h2 style="font-size: 1.3rem; color: #fff; margin: 0 0 16px;">Frequently Asked Questions About Orc</h2>
      <div style="display: flex; flex-direction: column; gap: 16px;">
        <div>
          <h3 style="font-size: 1.05rem; color: #c9a227; margin: 0 0 6px;">How does the Orc +12% Max HP multiplier interact with gear?</h3>
          <p style="color: var(--muted); font-size: 0.9rem; line-height: 1.5; margin: 0;">
            The Orc +12% Max HP multiplier applies to both base character health and flat health bonuses granted by equipped armor sets, providing massive exponential value in late-game plate builds.
          </p>
        </div>
        <div>
          <h3 style="font-size: 1.05rem; color: #c9a227; margin: 0 0 6px;">What are the spin odds for Orc from the Goblin Merchant?</h3>
          <p style="color: var(--muted); font-size: 0.9rem; line-height: 1.5; margin: 0;">
            Orc is an Uncommon/Rare lineage with a 15.0% spin rate. Most players can easily acquire Orc within 5 to 7 race spins, making it the most cost-effective melee lineage in Pixel Lineage.
          </p>
        </div>
        <div>
          <h3 style="font-size: 1.05rem; color: #c9a227; margin: 0 0 6px;">Does the Berserk Rage attack bonus remain active if healed above 30% HP?</h3>
          <p style="color: var(--muted); font-size: 0.9rem; line-height: 1.5; margin: 0;">
            No. The +15% attack bonus dynamically deactivates as soon as current character HP rises above 30.0% of maximum health.
          </p>
        </div>
      </div>
    </section>
"""
    },
    "elf": {
        "file": "src/pages/races/elf.astro",
        "insert_before": "<!-- Spin Economics -->",
        "color": "#22c55e",
        "milestone_table": """
      <!-- Level 1 to 30 Milestone Scaling Table -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #fff; margin: 0 0 14px;">Elf Level 1 to 30 Milestone Progression Ledger</h2>
        <p style="color: var(--muted); font-size: 0.95rem; line-height: 1.6; margin: 0 0 16px;">
          Elf provides unmatched critical strike precision and evasion agility. Here is the verified stat progression across seven key milestone levels, measured with standard Thief/Archer archetype scaling:
        </p>

        <div style="overflow-x: auto;">
          <table style="width: 100%; border-collapse: collapse; font-size: 0.88rem; text-align: left;">
            <thead>
              <tr style="background: #0d0a14; border-bottom: 2px solid var(--line); color: #c9a227;">
                <th style="padding: 10px 12px;">Level Milestone</th>
                <th style="padding: 10px 12px;">Base Crit Rate</th>
                <th style="padding: 10px 12px;">Elf Crit (+10%)</th>
                <th style="padding: 10px 12px;">Base Speed</th>
                <th style="padding: 10px 12px;">Dodge Chance</th>
                <th style="padding: 10px 12px;">Projectile Velocity</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 1 (Novice)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">12.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #22c55e;">22.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">12 SPD</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">5.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">+12.0%</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 5 (Apprentice)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">14.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #22c55e;">24.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">19 SPD</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">7.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">+12.0%</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 10 (Adept)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">16.5%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #22c55e;">26.5%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">27 SPD</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">9.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">+12.0%</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 15 (Super Class)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">19.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #22c55e;">29.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">36 SPD</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">11.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">+12.0%</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 20 (Master)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">21.5%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #22c55e;">31.5%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">45 SPD</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">13.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">+12.0%</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--line);">
                <td style="padding: 10px 12px; font-weight: 600; color: #fff;">Level 25 (Ultra Class)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">24.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #22c55e;">34.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">54 SPD</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">15.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">+12.0%</td>
              </tr>
              <tr>
                <td style="padding: 10px 12px; font-weight: 600; color: #22c55e;">Level 30 (Capstone)</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #f43f5e;">26.5%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #22c55e;">36.5%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #34d399;">63 SPD</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #38bdf8;">17.0%</td>
                <td style="padding: 10px 12px; font-family: var(--font-mono); color: #c9a227;">+12.0%</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- Boss Matchup Strategies -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #c9a227; margin: 0 0 16px;">Dungeon Boss Tactical Matchup Ledger</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px;">
          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #34d399;">
            <strong style="color: #34d399; font-size: 1rem; display: block; margin-bottom: 6px;">Goblin King (Act 1)</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              <strong>Advantage: Very High.</strong> Goblin King has slow turn speed. An Elf Archer acts twice before the King takes a single turn, consistently inflicting critical hits from long range outside the King's melee swing radius.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #38bdf8;">
            <strong style="color: #38bdf8; font-size: 1rem; display: block; margin-bottom: 6px;">Crypt Necromancer (Act 2)</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              <strong>Advantage: High.</strong> Elf's +12% projectile velocity pierces through summon swarms to target the Necromancer directly in the backline, eliminating the summoning core before minion counts become unmanageable.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #f43f5e;">
            <strong style="color: #f43f5e; font-size: 1rem; display: block; margin-bottom: 6px;">Abyssal Colossus (Act 3)</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              <strong>Advantage: Moderate.</strong> The Colossus's massive armor requires stacking critical multipliers to penetrate. Use Sniper Super Class precision shots combined with Keen Eye to reach 65%+ crit rates for maximum armor bypass.
            </p>
          </div>
        </div>
      </section>

      <!-- Best-in-Slot Equipment Loadout -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #fff; margin: 0 0 16px;">Recommended Best-in-Slot Equipment Synergies</h2>
        <div style="display: flex; flex-direction: column; gap: 14px;">
          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px;">
            <strong style="color: #22c55e;">Weapon: Ancient Elven Greatbow or Dual Stiletto</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Provides +32 ATK, +8% Crit Chance, and elevates critical multiplier from 1.5x to 1.8x. Capitalizes directly on Elf's high base critical probability.
            </p>
          </div>
          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px;">
            <strong style="color: #38bdf8;">Armor Set: Sylph Shadowgarb (Tier 3 Set)</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Provides +34 DEF, +14 SPD, and +10% Evasion. Pushes total character dodge chance past 25%, allowing the Elf to naturally evade a quarter of all incoming boss attacks.
            </p>
          </div>
          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px;">
            <strong style="color: #c9a227;">Accessory: Hawk-Eye Quiver of the Forest</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Increases maximum attack range by 1 grid tile and boosts projectile critical damage by 15%, solidifying long-range supremacy.
            </p>
          </div>
        </div>
      </section>

      <!-- Talent Pairing Synergies & Traps -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #c9a227; margin: 0 0 14px;">Talent Pairing Synergies & Anti-Synergies</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px;">
          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #34d399;">
            <strong style="color: #34d399; font-size: 0.95rem;">Must-Pick: Keen Eye + Bloodthirst</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 6px 0 0;">
              Keen Eye adds +5% Crit and +2% Dodge, pushing critical strike chance past 40%. Bloodthirst converts those frequent critical strikes into a 12% health leech engine.
            </p>
          </div>
          <div style="background: #0d0a14; padding: 16px; border-radius: 6px; border-left: 3px solid #f43f5e;">
            <strong style="color: #f43f5e; font-size: 0.95rem;">Trap Talent: Iron Soul</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 6px 0 0;">
              Elven defense stat growths are among the lowest in the game. Stacking percentage defense provides negligible mitigation compared to stacking Speed, Crit, or Dodge.
            </p>
          </div>
        </div>
      </section>
""",
        "faq_section": """
    <!-- Frequently Asked Questions About Elf -->
    <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
      <h2 style="font-size: 1.3rem; color: #fff; margin: 0 0 16px;">Frequently Asked Questions About Elf</h2>
      <div style="display: flex; flex-direction: column; gap: 16px;">
        <div>
          <h3 style="font-size: 1.05rem; color: #c9a227; margin: 0 0 6px;">Does Elf's +10% Critical Strike Chance apply to magic spells?</h3>
          <p style="color: var(--muted); font-size: 0.9rem; line-height: 1.5; margin: 0;">
            Yes. Elf's +10% critical bonus applies universally to physical attacks, archery shots, and offensive magic spells like Fireball or Arcane Missiles.
          </p>
        </div>
        <div>
          <h3 style="font-size: 1.05rem; color: #c9a227; margin: 0 0 6px;">What are the spin odds for Elf from the Goblin Merchant?</h3>
          <p style="color: var(--muted); font-size: 0.9rem; line-height: 1.5; margin: 0;">
            Elf occupies the Rare 10.0% tier in the Goblin Merchant spin pool. Players typically secure Elf within 10 race spins, offering strong early-game consistency.
          </p>
        </div>
        <div>
          <h3 style="font-size: 1.05rem; color: #c9a227; margin: 0 0 6px;">How does Forest Stride evasion calculate with character dodge?</h3>
          <p style="color: var(--muted); font-size: 0.9rem; line-height: 1.5; margin: 0;">
            Forest Stride provides a flat +5% bonus that adds directly to your base character dodge rate and any evasion bonuses granted by light leather armor sets.
          </p>
        </div>
      </div>
    </section>
"""
    }
}

for race_key, data in RACE_DATA.items():
    path = data["file"]
    if not os.path.exists(path):
        print(f"File not found: {path}")
        continue
    
    content = open(path).read()
    insert_marker = data["insert_before"]
    
    # Check if already enriched
    if "Level 1 to 30 Milestone Progression Ledger" in content:
        print(f"{race_key} already enriched, skipping.")
        continue
    
    if insert_marker not in content:
        print(f"Marker '{insert_marker}' not found in {path}!")
        continue
    
    # Insert milestone table and other sections before insert_marker
    new_middle = data["milestone_table"] + "\n      " + insert_marker
    content = content.replace(insert_marker, new_middle, 1)
    
    # Insert FAQ section before navigation
    nav_marker = "<!-- Navigation -->" if "<!-- Navigation -->" in content else "<!-- Cross-Linking -->"
    if nav_marker in content and "Frequently Asked Questions About" not in content:
        new_nav = data["faq_section"] + "\n      " + nav_marker
        content = content.replace(nav_marker, new_nav, 1)
    
    with open(path, "w") as f:
        f.write(content)
    print(f"Successfully enriched {race_key} at {path}")

print("Enrichment complete.")

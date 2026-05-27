# Extraction Schema Reference

Use this reference when producing a full visual design system extraction from images, screenshots, moodboards, cinematic stills, or brand/style frames.

## Required Top-Level Sections

Include these sections in this order for comprehensive outputs:

```yaml
meta:
source_analysis:
confidence_scores:
design_principles:
brand_identity:
character_identity:
art_direction:
visual_language:
color_system:
typography:
spacing:
layout:
grid_system:
sizing:
borders:
radii:
shadows:
gradients:
materials:
textures:
lighting:
motion:
animation:
camera:
composition:
environment:
setting:
wardrobe:
props:
iconography:
illustration_style:
photography_style:
cinematic_style:
rendering_style:
surface_treatment:
accessibility:
interaction_design:
ui_patterns:
sound_design:
narrative_tone:
emotional_palette:
worldbuilding:
styling_rules:
dos_and_donts:
token_dependencies:
dynamic_tokens:
responsive_rules:
state_variants:
platform_adaptations:
ai_generation_prompts:
implementation_notes:
```

If a section does not apply, keep the section and mark it as not applicable with evidence.

## Deterministic Nested Field Contract

Use the nested fields below as the canonical output shape. Keep the top-level order from the required section list. Within each section, keep the nested key order shown here. If a field is not supported by the references, keep the field and set `applicability: "not_applicable"`, `confidence: high`, and a grounded `inference_basis`.

```yaml
meta:
  schema_version: "1.0"
  extraction_mode: "comprehensive_visual_design_system"
  source_count: 0
  source_types: []
  generated_for: "ui_ux_brand_motion_creative_direction"
  validation:
    yaml_only: true
    parser_validated: true
    markdown_fences: false
source_analysis:
  observed: []
  inferred: []
  speculative: []
  source_inventory:
    images: []
    visible_text: []
    visible_interfaces: []
    visible_people_or_characters: []
    visible_environments: []
    visible_brand_marks: []
  evidence_boundaries:
    directly_observed: []
    inferred_from_visual_cues: []
    low_confidence_extrapolations: []
confidence_scores:
  overall: medium
  color_system: medium
  typography: medium
  layout: medium
  motion: low
  cinematic_language: medium
  ui_patterns: medium
  worldbuilding: medium
design_principles:
  core_tenets: []
  hierarchy_rules: []
  consistency_rules: []
  contrast_rules: []
  restraint_rules: []
  confidence: medium
  inference_basis: ""
brand_identity:
  positioning: ""
  personality_traits: []
  audience: []
  value_signals: []
  trust_signals: []
  differentiation: []
  confidence: medium
  inference_basis: ""
character_identity:
  applicability: "applicable"
  archetypes: []
  role_in_system: []
  personality_cues: []
  social_positioning: []
  grooming_and_presentation: []
  confidence: medium
  inference_basis: ""
art_direction:
  art_direction_summary: ""
  references_to_visual_cues: []
  production_value: ""
  cultural_references: []
  tactile_feel: []
  sensory_implications: []
  confidence: medium
  inference_basis: ""
visual_language:
  shape_language: []
  line_quality: []
  density: ""
  balance: ""
  rhythm: ""
  contrast: ""
  motif_library: []
  confidence: medium
  inference_basis: ""
color_system:
  primary: {}
  secondary: {}
  neutrals: {}
  accents: {}
  semantic: {}
  tonal_scales: {}
  contrast_hierarchy: []
  atmospheric_grading: []
  lut_cues: []
  accessibility_notes: []
typography:
  font_families:
    observed_or_implied: []
    primary:
      family: ""
      classification: ""
      fallback_stack: []
      visual_grounding: ""
      confidence: medium
      inference_basis: ""
    supporting:
      family: ""
      classification: ""
      fallback_stack: []
      pairing_logic: ""
      visual_grounding: ""
      confidence: medium
      inference_basis: ""
    rare_unique_candidates: []
  type_scale:
    display: {}
    heading: {}
    body: {}
    caption: {}
    microcopy: {}
  hierarchy:
    headline_rules: []
    body_rules: []
    label_rules: []
    emphasis_rules: []
  weights: {}
  leading: {}
  tracking: {}
  editorial_tone: ""
  accessibility: []
spacing:
  base_unit: ""
  scale: {}
  component_spacing: {}
  section_spacing: {}
  density_rules: []
layout:
  layout_principles: []
  alignment: []
  information_hierarchy: []
  content_grouping: []
  negative_space: []
grid_system:
  columns: {}
  gutters: {}
  margins: {}
  breakpoints: {}
  composition_grid: []
sizing:
  component_sizes: {}
  icon_sizes: {}
  media_sizes: {}
  touch_targets: {}
  responsive_scaling: []
borders:
  widths: {}
  styles: {}
  usage_rules: []
  contrast_behavior: []
radii:
  scale: {}
  usage_rules: []
  shape_personality: ""
shadows:
  elevation_scale: {}
  ambient_shadows: {}
  directional_shadows: {}
  usage_rules: []
gradients:
  linear: {}
  radial: {}
  atmospheric: {}
  usage_rules: []
materials:
  material_palette: []
  physical_properties: []
  ui_materials: []
  confidence: medium
  inference_basis: ""
textures:
  texture_types: []
  grain: ""
  surface_noise: ""
  pattern_language: []
lighting:
  lighting_direction: ""
  quality: ""
  contrast: ""
  color_temperature: ""
  practical_lights: []
  mood_effect: ""
motion:
  motion_principles: []
  durations: {}
  easing: {}
  choreography: []
  interaction_motion: {}
  camera_motion: {}
animation:
  entrance: {}
  exit: {}
  loading: {}
  feedback: {}
  state_change: {}
  reduced_motion: {}
camera:
  framing: []
  focal_length_tendencies: []
  depth_of_field: ""
  camera_movement: []
  stabilization: ""
  aspect_ratio: ""
composition:
  framing_rules: []
  focal_points: []
  balance: ""
  rhythm: ""
  cropping: []
  scale_relationships: []
environment:
  environment_type: ""
  architecture: []
  geography: []
  climate: []
  socioeconomic_tone: ""
  environmental_storytelling: []
setting:
  era: ""
  time_of_day: ""
  cultural_context: []
  technological_sophistication: ""
  narrative_function: ""
wardrobe:
  applicability: "applicable"
  palette: []
  silhouette: []
  materials: []
  styling_rules: []
  confidence: medium
  inference_basis: ""
props:
  prop_categories: []
  material_rules: []
  narrative_roles: []
  scale_rules: []
iconography:
  style: ""
  stroke_width: ""
  corner_style: ""
  filled_vs_outline: ""
  metaphor_rules: []
  accessibility_rules: []
illustration_style:
  applicability: "applicable"
  rendering_approach: ""
  linework: ""
  color_behavior: ""
  detail_level: ""
  confidence: medium
  inference_basis: ""
photography_style:
  applicability: "applicable"
  subject_treatment: ""
  lens_behavior: ""
  color_grading: ""
  composition: []
  retouching: ""
cinematic_style:
  genre_cues: []
  shot_language: []
  editorial_rhythm: ""
  aspect_ratio: ""
  grading: []
rendering_style:
  medium: ""
  realism_level: ""
  surface_modeling: []
  atmosphere: []
  post_processing: []
surface_treatment:
  finish: []
  reflectivity: ""
  translucency: ""
  wear: ""
  depth_treatment: []
accessibility:
  contrast_targets: []
  type_legibility: []
  motion_safety: []
  color_independence: []
  touch_targets: []
  alt_text_guidance: []
interaction_design:
  interaction_principles: []
  affordances: []
  feedback_rules: []
  input_methods: []
  error_behavior: []
ui_patterns:
  navigation: []
  controls: []
  cards_or_panels: []
  forms: []
  overlays: []
  data_display: []
  empty_states: []
sound_design:
  applicability: "applicable"
  sonic_palette: []
  feedback_sounds: []
  ambient_sound: ""
  rhythm: ""
  confidence: low
  inference_basis: ""
narrative_tone:
  tone_words: []
  pacing: ""
  point_of_view: ""
  stakes: ""
  emotional_arc: []
emotional_palette:
  primary_emotions: []
  secondary_emotions: []
  tension_release: []
  sensory_associations: []
worldbuilding:
  world_rules: []
  cultural_influences: []
  economy_and_status: []
  technology_rules: []
  environmental_logic: []
styling_rules:
  always: []
  prefer: []
  avoid: []
  conditional: []
dos_and_donts:
  dos: []
  donts: []
  edge_cases: []
token_dependencies:
  color_to_typography: []
  spacing_to_layout: []
  motion_to_interaction: []
  material_to_lighting: []
  brand_to_components: []
dynamic_tokens:
  modes: {}
  emotional_states: {}
  cinematic_intensity: {}
  seasonal_variants: {}
  interaction_states: {}
responsive_rules:
  mobile: {}
  tablet: {}
  desktop: {}
  wide: {}
  density_adjustments: []
state_variants:
  default: {}
  hover: {}
  active: {}
  focus: {}
  disabled: {}
  loading: {}
  error: {}
  success: {}
platform_adaptations:
  web: {}
  ios: {}
  android: {}
  print: {}
  ai_generation: {}
ai_generation_prompts:
  image_prompt: ""
  negative_prompt: ""
  style_prompt: ""
  motion_prompt: ""
  ui_prompt: ""
  consistency_rules: []
implementation_notes:
  tokenization_notes: []
  css_variable_guidance: []
  design_tool_guidance: []
  engineering_constraints: []
  validation_steps: []
```

## Nested Field Fill Details

Use these meanings when filling the deterministic skeleton. Each field should contain reference-grounded content, not generic design advice.

### Universal Field Shapes

Apply these shapes to every nested field before using the field-specific notes below:

- Scalar string fields: write one concise, evidence-backed sentence or phrase. Include the visible cue, not just the abstract conclusion.
- List fields: use a list of strings for simple observations; use a list of mappings when items need `value`, `usage`, `confidence`, or `inference_basis`.
- Mapping fields ending in token groups, scales, or variants: use semantic child keys, each with `value`, `usage`, `confidence`, and `inference_basis`.
- `confidence` fields: use only `low`, `medium`, or `high`.
- `inference_basis` fields: name the exact visual cue, source region, or repeated pattern that supports the value.
- `applicability` fields: use `applicable`, `not_applicable`, or `inferred`, then keep `confidence` and `inference_basis` beside it.
- Empty values: avoid bare `""`, `[]`, or `{}` in final comprehensive output unless the field is truly not applicable; prefer a not-applicable object with evidence.
- Cross-reference fields: when one field depends on another, name the dependency explicitly, such as `color_system.neutrals.neutral_950` or `typography.font_families.primary`.

### Standard Token Object

Use this object shape for color, spacing, type, sizing, border, radius, shadow, gradient, motion, state, responsive, and platform tokens unless a field-specific shape is given:

```yaml
token_name:
  value: "Concrete value, range, or descriptive value."
  usage: "Where this token should be used."
  visual_grounding: "Visible cue from the reference images."
  confidence: medium
  inference_basis: "Why this token follows from the references."
```

For color tokens, extend the standard shape with `hex`, `rgb`, and `hsl`. For motion tokens, extend it with `duration`, `easing`, and `trigger` when relevant. For typography tokens, extend it with `family`, `size`, `line_height`, `weight`, `tracking`, or `fallback_stack` as relevant.

### Evidence And Confidence

- `meta.schema_version`: Use the version of this extraction schema, currently `"1.0"`.
- `meta.extraction_mode`: Use `"comprehensive_visual_design_system"` for full outputs, or a narrower snake_case mode only when the user requests a partial extraction.
- `meta.source_count`: Count the analyzed visual references.
- `meta.source_types`: List media types such as `screenshot`, `moodboard`, `photographic_still`, `cinematic_frame`, `brand_board`, or `ui_capture`.
- `meta.generated_for`: Name the intended downstream uses, keeping `ui_ux_brand_motion_creative_direction` for comprehensive outputs.
- `meta.validation.yaml_only`: Set `true` when the response contains only YAML.
- `meta.validation.parser_validated`: Set `true` only after `scripts/validate_design_system_yaml.py` or an equivalent YAML parser succeeds.
- `meta.validation.markdown_fences`: Set `false`; final output must not include code fences.
- `source_analysis.observed`: List facts directly visible in the references.
- `source_analysis.inferred`: List system rules derived from visible patterns.
- `source_analysis.speculative`: List useful low-confidence extrapolations that are not directly visible.
- `source_analysis.source_inventory.images`: List each source with id, type, approximate subject, and notable visual regions when possible.
- `source_analysis.source_inventory.visible_text`: Capture readable text, labels, headings, numerals, and typography clues.
- `source_analysis.source_inventory.visible_interfaces`: Capture visible UI surfaces, controls, navigation, data views, or app shells.
- `source_analysis.source_inventory.visible_people_or_characters`: Capture people, characters, pose, expression, wardrobe, and social signals.
- `source_analysis.source_inventory.visible_environments`: Capture physical or digital settings, architecture, geography, and atmosphere.
- `source_analysis.source_inventory.visible_brand_marks`: Capture logos, marks, product names, symbols, and repeated brand motifs.
- `source_analysis.evidence_boundaries.directly_observed`: Repeat high-impact evidence that should constrain all later inference.
- `source_analysis.evidence_boundaries.inferred_from_visual_cues`: State the visual cues used for inference.
- `source_analysis.evidence_boundaries.low_confidence_extrapolations`: State where the output is intentionally speculative.
- `confidence_scores.*`: Use `low`, `medium`, or `high` to summarize confidence for each major domain.

### Strategy And Identity

- `design_principles.core_tenets`: List durable design rules that the whole system should obey.
- `design_principles.hierarchy_rules`: Explain how attention, scale, contrast, and sequence are controlled.
- `design_principles.consistency_rules`: Explain repeated rules across color, type, surfaces, imagery, and layout.
- `design_principles.contrast_rules`: Explain contrast in color, type, material, lighting, pacing, and density.
- `design_principles.restraint_rules`: Explain what the system intentionally avoids or keeps quiet.
- `design_principles.confidence` and `design_principles.inference_basis`: Ground the section in visible evidence.
- `brand_identity.positioning`: Infer the brand/category posture such as luxury, utility, editorial, cinematic, playful, technical, institutional, or rebellious.
- `brand_identity.personality_traits`: List stable personality adjectives backed by visual evidence.
- `brand_identity.audience`: Infer likely users or viewers and their sophistication level.
- `brand_identity.value_signals`: Identify signals of quality, speed, craft, safety, intelligence, status, warmth, or precision.
- `brand_identity.trust_signals`: Identify credibility cues such as restraint, consistency, materials, data clarity, realism, or institutional tone.
- `brand_identity.differentiation`: Explain what feels distinct compared with generic category defaults.
- `brand_identity.confidence` and `brand_identity.inference_basis`: Ground the brand read.
- `character_identity.applicability`: Use `applicable` only when characters or people appear or are clearly implied.
- `character_identity.archetypes`: Name visual archetypes such as operator, founder, explorer, archivist, athlete, monarch, technician, or outsider.
- `character_identity.role_in_system`: Explain how characters support brand, story, world, UI, or marketing.
- `character_identity.personality_cues`: Extract demeanor from expression, pose, styling, activity, and framing.
- `character_identity.social_positioning`: Infer status, profession, group membership, authority, or social role.
- `character_identity.grooming_and_presentation`: Describe hair, makeup, grooming, polish, and intentional dishevelment.
- `character_identity.confidence` and `character_identity.inference_basis`: Ground character claims.

### Art Direction And Visual Language

- `art_direction.art_direction_summary`: Give a concise, reusable creative direction statement.
- `art_direction.references_to_visual_cues`: List concrete image cues that justify the art direction.
- `art_direction.production_value`: Infer whether the visual language feels lo-fi, polished, cinematic, editorial, premium, handmade, technical, or mass-market.
- `art_direction.cultural_references`: Name broad cultural or era cues only when visible evidence supports them.
- `art_direction.tactile_feel`: Describe perceived touch qualities such as soft, sharp, glassy, dusty, metallic, rubberized, paperlike, or worn.
- `art_direction.sensory_implications`: Capture implied sound, temperature, smell, weight, and texture where visually supported.
- `art_direction.confidence` and `art_direction.inference_basis`: Ground the section.
- `visual_language.shape_language`: Describe dominant forms such as geometric, organic, rectilinear, circular, angular, modular, elongated, or irregular.
- `visual_language.line_quality`: Describe strokes, edges, contours, outlines, and precision.
- `visual_language.density`: State whether the system is sparse, dense, layered, airy, compressed, or maximal.
- `visual_language.balance`: Describe symmetry, asymmetry, weight distribution, and visual stability.
- `visual_language.rhythm`: Describe repetition, cadence, spacing intervals, and scan pattern.
- `visual_language.contrast`: Describe value, scale, texture, type, and spatial contrast.
- `visual_language.motif_library`: List recurring symbols, shapes, image tropes, UI marks, or material cues.
- `visual_language.confidence` and `visual_language.inference_basis`: Ground the read.

### Foundation Tokens

- `color_system.primary`, `secondary`, `neutrals`, `accents`, and `semantic`: Use token objects with `hex`, `rgb`, `hsl`, `usage`, `confidence`, and `inference_basis`.
- `color_system.tonal_scales`: Define reusable scales such as `neutral_50` through `neutral_950` when enough evidence exists.
- `color_system.contrast_hierarchy`: Explain foreground/background and emphasis contrast rules.
- `color_system.atmospheric_grading`: Describe haze, color cast, shadow tint, highlight tint, and environmental color.
- `color_system.lut_cues`: Infer cinematic grade cues such as bleach bypass, teal shadows, warm highlights, muted chroma, or lifted blacks.
- `color_system.accessibility_notes`: Note contrast risks and accessible substitutions.
- `typography.font_families.observed_or_implied`: List visible or likely families with role, confidence, and evidence.
- `typography.font_families.primary`: Define the main family for body/interface use with `family`, `classification`, `fallback_stack`, `visual_grounding`, `confidence`, and `inference_basis`.
- `typography.font_families.supporting`: Define the complementary family with `pairing_logic` and grounding.
- `typography.font_families.rare_unique_candidates`: Provide rare, distinctive, evidence-grounded candidates with family, role, classification, fallback stack, pairings, visual grounding, rarity reason, pairing logic, use constraints, confidence, and inference basis.
- `typography.type_scale.display`, `heading`, `body`, `caption`, and `microcopy`: Use token objects with size, line height, weight, tracking, usage, and confidence.
- `typography.hierarchy.headline_rules`, `body_rules`, `label_rules`, and `emphasis_rules`: State how type creates reading order and emphasis.
- `typography.weights`: Map semantic weights such as `regular`, `medium`, `semibold`, `bold`, or `display`.
- `typography.leading`: Map line-height tokens by text role.
- `typography.tracking`: Map letter-spacing rules by text role; avoid negative tracking unless visibly supported.
- `typography.editorial_tone`: Describe the written voice implied by the type system.
- `typography.accessibility`: Capture legibility, minimum sizes, contrast, and fallback concerns.
- `spacing.base_unit`: Infer the base spacing increment, such as `4px`, `6px`, or `8px`.
- `spacing.scale`: Define named spacing tokens with values and usage.
- `spacing.component_spacing`: Define padding/gap rules inside components.
- `spacing.section_spacing`: Define page or scene-level spacing intervals.
- `spacing.density_rules`: Explain compact, standard, and spacious density variants.
- `layout.layout_principles`: State layout rules such as editorial stacking, dashboard density, centered composition, cinematic framing, or modular panels.
- `layout.alignment`: Define alignment anchors and exceptions.
- `layout.information_hierarchy`: Explain scan order and priority levels.
- `layout.content_grouping`: Explain grouping by proximity, panels, bands, frames, or visual clusters.
- `layout.negative_space`: Describe how empty space is used for focus and pacing.
- `grid_system.columns`, `gutters`, `margins`, and `breakpoints`: Define responsive grid values and confidence.
- `grid_system.composition_grid`: Describe non-UI composition grids such as thirds, centerline, horizon, vanishing point, or poster grid.
- `sizing.component_sizes`, `icon_sizes`, `media_sizes`, and `touch_targets`: Define size tokens with usage and platform notes.
- `sizing.responsive_scaling`: Explain how sizes change across mobile, tablet, desktop, and wide screens.

### Surface And Material Tokens

- `borders.widths`: Define border width tokens and their roles.
- `borders.styles`: Define solid, translucent, dashed, hairline, inset, or image-edge border behavior.
- `borders.usage_rules`: Explain where borders appear or are avoided.
- `borders.contrast_behavior`: Explain how borders adapt on light, dark, busy, or photographic backgrounds.
- `radii.scale`: Define corner-radius tokens and values.
- `radii.usage_rules`: Map radius tokens to components, cards, media, controls, and containers.
- `radii.shape_personality`: Explain whether corners feel sharp, utilitarian, soft, friendly, mechanical, or luxurious.
- `shadows.elevation_scale`: Define depth tokens with blur, spread, opacity, and usage.
- `shadows.ambient_shadows`: Describe diffuse environmental shadow behavior.
- `shadows.directional_shadows`: Describe directional cast shadows and light-source logic.
- `shadows.usage_rules`: Explain when shadows are used, avoided, or replaced by borders/material.
- `gradients.linear`, `radial`, and `atmospheric`: Define gradient tokens and usage.
- `gradients.usage_rules`: Explain where gradients support depth, lighting, emotion, or state.
- `materials.material_palette`: List visual materials such as glass, brushed metal, matte plastic, concrete, paper, leather, fabric, water, or neon.
- `materials.physical_properties`: Describe weight, reflectivity, opacity, softness, age, and durability.
- `materials.ui_materials`: Translate physical materials into UI surfaces.
- `materials.confidence` and `materials.inference_basis`: Ground material claims.
- `textures.texture_types`: List texture categories visible or implied.
- `textures.grain`: Describe grain size, intensity, and distribution.
- `textures.surface_noise`: Describe noise, patina, scratches, bloom, compression, or analog artifacts.
- `textures.pattern_language`: Describe repeated texture patterns or motifs.
- `lighting.lighting_direction`: Identify key light direction or UI lighting logic.
- `lighting.quality`: Describe soft, hard, diffuse, specular, practical, overcast, neon, or studio light.
- `lighting.contrast`: Describe high-key, low-key, chiaroscuro, flat, or balanced contrast.
- `lighting.color_temperature`: Describe warm, cool, mixed, sodium, fluorescent, daylight, or neutral temperature.
- `lighting.practical_lights`: List visible or implied light sources.
- `lighting.mood_effect`: Explain how lighting changes emotion and attention.

### Motion, Camera, And Composition

- `motion.motion_principles`: State motion personality such as precise, slow, elastic, mechanical, cinematic, restrained, or playful.
- `motion.durations`: Define duration tokens for micro, standard, emphasized, scene, and ambient motions.
- `motion.easing`: Define easing tokens and intended use.
- `motion.choreography`: Explain sequence, delay, stagger, reveal, and exit rules.
- `motion.interaction_motion`: Define motion for hover, press, focus, drag, selection, navigation, and feedback.
- `motion.camera_motion`: Define pan, push, orbit, handheld, locked-off, zoom, dolly, or parallax behavior.
- `animation.entrance`, `exit`, `loading`, `feedback`, `state_change`, and `reduced_motion`: Define animation tokens for each state, including reduced-motion substitutes.
- `camera.framing`: Describe close-up, wide, centered, off-axis, over-the-shoulder, macro, or establishing framings.
- `camera.focal_length_tendencies`: Infer wide, normal, telephoto, macro, anamorphic, or compressed lens tendencies.
- `camera.depth_of_field`: Describe shallow, deep, rack-focus, background blur, or crisp UI treatment.
- `camera.camera_movement`: Describe likely movement style.
- `camera.stabilization`: State handheld, locked, stabilized, floaty, mechanical, or shaky.
- `camera.aspect_ratio`: State likely aspect ratio or responsive frame behavior.
- `composition.framing_rules`: Explain how subjects are placed in the frame.
- `composition.focal_points`: List primary and secondary attention targets.
- `composition.balance`: Describe visual weight and stability.
- `composition.rhythm`: Describe repeated intervals, cuts, panels, or object cadence.
- `composition.cropping`: Explain crop style and edge tension.
- `composition.scale_relationships`: Explain relationships between hero elements, text, people, props, and UI.

### World, People, And Object Systems

- `environment.environment_type`: Name the environment category such as studio, street, interior, wilderness, interface, industrial, domestic, retail, or abstract.
- `environment.architecture`, `geography`, and `climate`: Extract built, natural, regional, weather, and atmosphere clues.
- `environment.socioeconomic_tone`: Infer status, resource level, scarcity, luxury, institutional tone, or working context.
- `environment.environmental_storytelling`: Explain what the setting implies about the world.
- `setting.era`: Infer historical, contemporary, retro-future, future, timeless, or mixed era.
- `setting.time_of_day`: Infer dawn, day, dusk, night, artificial, or ambiguous time cues.
- `setting.cultural_context`: Capture visible cultural codes without overclaiming.
- `setting.technological_sophistication`: Infer analog, digital, high-tech, low-tech, industrial, magical, or speculative tech level.
- `setting.narrative_function`: Explain why the setting exists in the system.
- `wardrobe.applicability`, `palette`, `silhouette`, `materials`, `styling_rules`, `confidence`, and `inference_basis`: Extract clothing rules when people or characters appear.
- `props.prop_categories`: Group objects by role such as tools, weapons, devices, documents, vessels, furniture, signage, or accessories.
- `props.material_rules`: Explain prop materials and finishes.
- `props.narrative_roles`: Explain what props communicate.
- `props.scale_rules`: Explain prop scale relative to people, UI, or environment.

### Image, UI, And Media Styles

- `iconography.style`: Define icon family style such as outline, filled, duotone, glyph, pictogram, technical, or hand-drawn.
- `iconography.stroke_width`: Define stroke weight tokens or relative thickness.
- `iconography.corner_style`: Define icon corner treatment.
- `iconography.filled_vs_outline`: Explain when to use filled or outline icons.
- `iconography.metaphor_rules`: Define metaphor complexity and object language.
- `iconography.accessibility_rules`: Define label, contrast, and size rules.
- `illustration_style.applicability`, `rendering_approach`, `linework`, `color_behavior`, `detail_level`, `confidence`, and `inference_basis`: Define illustration rules only when visible or implied.
- `photography_style.applicability`: Mark whether photographic treatment is visible or needed.
- `photography_style.subject_treatment`: Describe posing, realism, retouching, distance, and subject dignity.
- `photography_style.lens_behavior`: Describe lens look from visible evidence.
- `photography_style.color_grading`: Describe photographic grade.
- `photography_style.composition`: Define photographic composition rules.
- `photography_style.retouching`: Describe skin, product, texture, cleanup, grain, and polish.
- `cinematic_style.genre_cues`: List cinematic genre cues supported by evidence.
- `cinematic_style.shot_language`: Define shot types and cut logic.
- `cinematic_style.editorial_rhythm`: Describe pacing and sequence feel.
- `cinematic_style.aspect_ratio`: Define cinematic frame ratio or responsive crop.
- `cinematic_style.grading`: Define color grade behavior.
- `rendering_style.medium`: Name medium such as real photography, 3D render, illustration, collage, vector, game engine, or mixed media.
- `rendering_style.realism_level`: Define abstract, stylized, semi-real, photoreal, hyperreal, or documentary realism.
- `rendering_style.surface_modeling`: Describe rendering of material, light, shadow, and geometry.
- `rendering_style.atmosphere`: Describe haze, bloom, particles, fog, depth, and air.
- `rendering_style.post_processing`: Describe grain, blur, chromatic aberration, halation, sharpening, or compression.
- `surface_treatment.finish`, `reflectivity`, `translucency`, `wear`, and `depth_treatment`: Define visible or implied surface finishing rules.

### Product, Accessibility, And Interaction

- `accessibility.contrast_targets`: Define contrast requirements and risk areas.
- `accessibility.type_legibility`: Define size, weight, tracking, and line-height constraints.
- `accessibility.motion_safety`: Define reduced-motion rules and motion risk.
- `accessibility.color_independence`: Define non-color indicators for state and hierarchy.
- `accessibility.touch_targets`: Define minimum target size and spacing.
- `accessibility.alt_text_guidance`: Define how visual assets should be described.
- `interaction_design.interaction_principles`: State interaction rules such as direct, calm, playful, precise, forgiving, or cinematic.
- `interaction_design.affordances`: Define how clickable, draggable, selectable, expandable, and editable elements signal behavior.
- `interaction_design.feedback_rules`: Define visual, motion, haptic, audio, or textual feedback.
- `interaction_design.input_methods`: Define mouse, touch, keyboard, stylus, gamepad, voice, or camera assumptions.
- `interaction_design.error_behavior`: Define error tone, recovery, and visual treatment.
- `ui_patterns.navigation`: Define navigation structure, active states, hierarchy, and density.
- `ui_patterns.controls`: Define button, toggle, slider, menu, tab, picker, and input style.
- `ui_patterns.cards_or_panels`: Define containers only when functionally needed.
- `ui_patterns.forms`: Define labels, validation, helper text, spacing, and input states.
- `ui_patterns.overlays`: Define modal, popover, drawer, tooltip, and sheet behavior.
- `ui_patterns.data_display`: Define tables, charts, metrics, maps, timelines, or graph treatment.
- `ui_patterns.empty_states`: Define tone, illustration, action, and density for empty or loading content.

### Narrative, Sound, Variants, And Implementation

- `sound_design.applicability`: Use `applicable` only when sound is visible, requested, or strongly implied.
- `sound_design.sonic_palette`: Describe timbre, texture, instruments, synthesis, room tone, or interface sounds.
- `sound_design.feedback_sounds`: Define sounds for success, error, selection, warning, transition, or loading.
- `sound_design.ambient_sound`: Infer background ambience.
- `sound_design.rhythm`: Map sound cadence to motion or editing cadence.
- `sound_design.confidence` and `sound_design.inference_basis`: Ground sound inference.
- `narrative_tone.tone_words`: List grounded narrative adjectives.
- `narrative_tone.pacing`: Describe story speed and reveal cadence.
- `narrative_tone.point_of_view`: Infer observer, participant, omniscient, product-led, character-led, or documentary view.
- `narrative_tone.stakes`: Infer emotional, commercial, social, technical, or narrative stakes.
- `narrative_tone.emotional_arc`: Describe how the system moves from one emotion to another.
- `emotional_palette.primary_emotions`, `secondary_emotions`, `tension_release`, and `sensory_associations`: Map emotion to visible cues and sensory implications.
- `worldbuilding.world_rules`: Define repeatable logic for the world.
- `worldbuilding.cultural_influences`: Capture broad cultural signals with confidence.
- `worldbuilding.economy_and_status`: Infer power, scarcity, abundance, class, and value systems.
- `worldbuilding.technology_rules`: Define how technology appears and behaves.
- `worldbuilding.environmental_logic`: Define how environment, climate, and materials constrain the world.
- `styling_rules.always`, `prefer`, `avoid`, and `conditional`: Provide prescriptive rules for maintaining the visual system.
- `dos_and_donts.dos`, `donts`, and `edge_cases`: Provide practical production guidance.
- `token_dependencies.color_to_typography`, `spacing_to_layout`, `motion_to_interaction`, `material_to_lighting`, and `brand_to_components`: Explain cross-token dependencies and constraints.
- `dynamic_tokens.modes`, `emotional_states`, `cinematic_intensity`, `seasonal_variants`, and `interaction_states`: Define contextual token variants using nested token objects.
- `responsive_rules.mobile`, `tablet`, `desktop`, and `wide`: Define platform-specific layout, density, type, and interaction changes.
- `responsive_rules.density_adjustments`: Define compact, regular, and spacious variants.
- `state_variants.default`, `hover`, `active`, `focus`, `disabled`, `loading`, `error`, and `success`: Define state-specific tokens and behavior.
- `platform_adaptations.web`, `ios`, `android`, `print`, and `ai_generation`: Translate the same visual system into each platform.
- `ai_generation_prompts.image_prompt`: Write a positive image-generation prompt that preserves the design system.
- `ai_generation_prompts.negative_prompt`: List visual failures to avoid.
- `ai_generation_prompts.style_prompt`: Condense style, mood, material, typography, and composition into reusable prompt language.
- `ai_generation_prompts.motion_prompt`: Describe animation or video generation behavior.
- `ai_generation_prompts.ui_prompt`: Describe UI generation constraints.
- `ai_generation_prompts.consistency_rules`: List rules for repeated generations.
- `implementation_notes.tokenization_notes`: Explain how to convert the YAML into tokens.
- `implementation_notes.css_variable_guidance`: Provide CSS variable naming and grouping guidance.
- `implementation_notes.design_tool_guidance`: Explain use in Figma, design tokens, or design system libraries.
- `implementation_notes.engineering_constraints`: Identify technical constraints, performance risks, responsive constraints, and accessibility requirements.
- `implementation_notes.validation_steps`: List checks for visual, YAML, accessibility, and implementation parity.

## YAML Syntax Rules

The final answer must be valid YAML that can be parsed by a standard YAML parser.

- Use spaces only for indentation.
- Use two-space indentation consistently.
- Do not use tabs anywhere.
- Do not repeat the same key within a mapping.
- Quote strings that contain `: `, `#`, `%`, `{`, `}`, `[`, `]`, leading zeros, or values that could be parsed as booleans.
- Use explicit empty mappings only when intentional: `{}`.
- Prefer mappings with `applicability`, `confidence`, and `inference_basis` over null section placeholders.
- Keep the YAML root as a mapping.
- Never include markdown fences in the final answer.

## Final Self-Check

Before returning the YAML, verify:

- The response contains YAML only.
- The YAML has been parsed by `scripts/validate_design_system_yaml.py` when tool access is available.
- The root is a mapping, not a list.
- There are no tab characters or duplicate keys.
- The top-level sections are present in the required order unless the user requested a narrower schema.
- Direct observations, inferences, and speculative extrapolations are separated.
- Ambiguous claims include `confidence` and `inference_basis`.
- Color tokens include HEX, RGB, HSL, usage, and confidence when color is inferred.
- `typography.font_families.rare_unique_candidates` contains specific rare family candidates with visual grounding, pairing logic, rarity reason, fallback stacks, and confidence.
- The system reads like a reusable design system, not a caption or image description.
- The output is internally consistent across brand, UI, motion, cinematic, and generation sections.

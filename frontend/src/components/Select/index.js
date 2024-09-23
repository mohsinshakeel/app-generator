import React from "react";
import './index.css'

const SelectDropdown = ({ options, value, onChange }) => {
  return (
    <select value={value} onChange={onChange} className="select-dropdown">
      <option value="" disabled>
        Show Files
      </option>
      {options.map((option, index) => (
        <option key={index} value={option.value}>
          {option.label}
        </option>
      ))}
    </select>
  );
};

export default SelectDropdown;
